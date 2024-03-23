import pandas as pd
import numpy as np

def criar_evento_chuvoso(df):
    # Calculate if each row is the start of an event
    df['evento_inicio'] = (df['acumulado_chuva_480_min'] != 0) & (df['acumulado_chuva_480_min'].shift(1) == 0)
    
    # Create a series to represent the event numbers
    evento_nums = df['evento_inicio'].cumsum()
    
    # Create the event IDs
    df['evento_chuvoso'] = df['id_estacao'].astype(str) + '_evento_' + evento_nums.map(str)
    
    # Filter out non-event rows
    df['evento_chuvoso'] = np.where(df['acumulado_chuva_480_min'] == 0, np.nan, df['evento_chuvoso'])
    
    # Drop intermediate columns
    df.drop(columns=['evento_inicio'], inplace=True)
    
    return df


def processamento_acumulado_chuva(df):
    dfs_estacoes = []
    estacoes = df["id_estacao"].unique().tolist()

    for estacao in estacoes:
        df_estacao = df[df['id_estacao'] == estacao].copy()
        mapping_dicts = []

        for intervalo in [30, 45, 90, 120, 360, 480, 720]:
            window_num = int(intervalo/15)
            df_estacao[f'acumulado_chuva_{intervalo}_min'] = df_estacao["acumulado_chuva_15_min"].rolling(window=window_num).sum()
            mapping_dict = df_estacao.set_index('primary_key')[f'acumulado_chuva_{intervalo}_min'].to_dict()
            mapping_dicts.append(mapping_dict)

        df_estacao.fillna(0, inplace=True)
        dfs_estacoes.append(df_estacao)

    dfs_estacoes = list(map(criar_evento_chuvoso, dfs_estacoes))
    df = pd.concat(dfs_estacoes)
    return df

def ordenar_colunas(df):
    colunas_ordenadas = [
    'primary_key','id_estacao', 'acumulado_chuva_15_min', 'acumulado_chuva_30_min','acumulado_chuva_45_min','acumulado_chuva_1_h','acumulado_chuva_90_min',
    'acumulado_chuva_120_min', 'acumulado_chuva_4_h', 'acumulado_chuva_360_min','acumulado_chuva_480_min', 'acumulado_chuva_720_min','acumulado_chuva_24_h',
    'acumulado_chuva_96_h','horario','data_particao','data_hora', 'evento_chuvoso']
    df = df[colunas_ordenadas]
    return df

def converte_mm_por_h(df):
    colunas_tempo = ['acumulado_chuva_15_min',
    'acumulado_chuva_30_min',
    'acumulado_chuva_45_min',
    'acumulado_chuva_90_min',
    'acumulado_chuva_120_min',
    'acumulado_chuva_1_h',
    'acumulado_chuva_4_h',
    'acumulado_chuva_24_h',
    'acumulado_chuva_96_h',
    'acumulado_chuva_360_min',
    'acumulado_chuva_480_min',
    'acumulado_chuva_720_min']

    for element in colunas_tempo:
        if element[-1] == 'h':
            horas = int(element.split('_')[-2])
            df[element] = df[element]/horas
        else:
            minutos_h = int(element.split('_')[-2])/60
            df[element] = df[element]/minutos_h
    
    return df

def encontra_chuvas_mais_fortes(df, coluna_tempo, data_inicio=None, data_fim=None, quantidade_eventos=10, id_estacao=None):
    # Filtrar o DataFrame pelas datas de início e fim, se fornecidas
    if data_inicio is not None and data_fim is not None:
        df = df[(df['data_particao'] >= data_inicio) & (df['data_particao'] <= data_fim)]
    elif data_inicio is not None:
        df = df[df['data_particao'] >= data_inicio]
    elif data_fim is not None:
        df = df[df['data_particao'] <= data_fim]
    
    # Filtrar o DataFrame pela estação, se fornecido
    if id_estacao is not None:
        df = df[df['id_estacao'] == id_estacao]
    
     # Ordenar o DataFrame pela coluna de tempo especificada
    df_ordenado = df.sort_values(by=coluna_tempo, ascending=False)
    
    # Retornar os x primeiros elementos diferentes da coluna 'evento_chuvoso'
    chuvas_fortes = df_ordenado['evento_chuvoso'].drop_duplicates().head(quantidade_eventos).tolist()
    
    # Retornar o DataFrame filtrado apenas com esses eventos
    df_eventos = df[df['evento_chuvoso'].isin(chuvas_fortes)]

    dados_ranking = {}
    for evento_chuvoso in chuvas_fortes:
        df_filtrado = df_eventos[df_eventos["evento_chuvoso"] == evento_chuvoso]
        
        # Ordenando o DataFrame por 'data_hora' em ordem ascendente
        df_filtrado = df_filtrado.sort_values(by='data_hora', ascending=True)
        
        # Pegando a data de início do evento
        data_inicio = df_filtrado['data_hora'].iloc[0]
        
        # Pegando a data de término do evento
        data_fim = df_filtrado['data_hora'].iloc[-1]
        
        # Ordenando o DataFrame por 'acumulado_chuva_1_h' em ordem descendente
        df_filtrado = df_filtrado.sort_values(by='acumulado_chuva_1_h', ascending=False)
        
        # Pegando a maior quantidade de chuva acumulada em 1 hora durante o evento
        maior_chuva_evento = df_filtrado["acumulado_chuva_1_h"].iloc[0]
        
        # Armazenando os resultados no dicionário dados_ranking
        dados_ranking[f"{evento_chuvoso}"] = [data_inicio, data_fim, maior_chuva_evento]
    
    return chuvas_fortes, df_eventos, dados_ranking