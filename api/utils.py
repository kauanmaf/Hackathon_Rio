import pandas as pd
import numpy as np
from datetime import datetime


def criar_evento_chuvoso(df):
    """
    Cria eventos chuvosos com base na coluna 'acumulado_chuva_480_min'.

    Parameters:
    - df (DataFrame): DataFrame contendo os dados a serem processados.

    Returns:
    - DataFrame: DataFrame com uma nova coluna 'evento_chuvoso' indicando o evento chuvoso associado a cada linha.

    Documentation:
    Esta função identifica eventos chuvosos com base na coluna 'acumulado_chuva_480_min' do DataFrame fornecido.
    Um evento chuvoso é considerado iniciado quando há acumulação de chuva após um período de ausência.
    Cada evento é identificado por um ID único composto pelo ID da estação e um número sequencial de evento.
    As linhas que não fazem parte de um evento chuvoso são marcadas com NaN na coluna 'evento_chuvoso'.

    Exemplo de Uso:
    >>> df_eventos = criar_evento_chuvoso(df_dados)
    """
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
    """
    Realiza o processamento de acumulado de chuva em um DataFrame por estação.

    Parameters:
    - df (DataFrame): DataFrame contendo os dados de precipitação por estação.

    Returns:
    - DataFrame: DataFrame resultante após o processamento de acumulado de chuva.

    Documentation:
    Esta função realiza o processamento de acumulado de chuva em um DataFrame, dividindo os dados por estação e aplicando a soma móvel em diferentes intervalos de tempo.
    Para cada estação, o acumulado de chuva é calculado para intervalos de 30, 45, 90, 120, 360, 480 e 720 minutos, utilizando a coluna 'acumulado_chuva_15_min' como base.
    Após o cálculo do acumulado de chuva, a função 'criar_evento_chuvoso' é aplicada para identificar e marcar os eventos chuvosos em cada estação.
    O resultado final é um DataFrame contendo os dados processados.

    Example:
    >>> df_processado = processamento_acumulado_chuva(df_dados)
    """
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
    """
    Ordena as colunas de um DataFrame de acordo com uma ordem específica.

    Parameters:
    - df (DataFrame): DataFrame contendo os dados a serem ordenados.

    Returns:
    - DataFrame: DataFrame com as colunas ordenadas.

    Documentation:
    Esta função recebe um DataFrame e reordena suas colunas de acordo com uma ordem específica.
    As colunas são ordenadas conforme a lista 'colunas_ordenadas', onde 'primary_key' e 'id_estacao' são mantidas no início,
    seguidas pelas colunas de acumulado de chuva em diferentes intervalos de tempo, e depois pelas colunas restantes, incluindo 'horario', 'data_particao', 'data_hora' e 'evento_chuvoso'.

    Exemplo de Uso:
    >>> df_ordenado = ordenar_colunas(df_dados)
    """
    colunas_ordenadas = [
    'primary_key','id_estacao', 'acumulado_chuva_15_min', 'acumulado_chuva_30_min','acumulado_chuva_45_min','acumulado_chuva_1_h','acumulado_chuva_90_min',
    'acumulado_chuva_120_min', 'acumulado_chuva_4_h', 'acumulado_chuva_360_min','acumulado_chuva_480_min', 'acumulado_chuva_720_min','acumulado_chuva_24_h',
    'acumulado_chuva_96_h','horario','data_particao','data_hora', 'evento_chuvoso']
    df = df[colunas_ordenadas]
    return df

def converte_mm_por_h(df):
    """
    Converte as unidades de medida de acumulado de chuva de mm para mm/h.

    Parameters:
    - df (DataFrame): DataFrame contendo os dados de acumulado de chuva em mm.

    Returns:
    - DataFrame: DataFrame com os dados de acumulado de chuva convertidos para mm/h.

    Documentation:
    Esta função recebe um DataFrame contendo dados de acumulado de chuva em milímetros (mm) e converte esses valores para milímetros por hora (mm/h).
    A conversão é aplicada a todas as colunas de acumulado de chuva especificadas em 'colunas_tempo', dividindo os valores pela quantidade de horas correspondente ao intervalo de tempo.
    Por exemplo, para as colunas com intervalo de tempo expresso em horas, os valores são divididos pelo número de horas. Para as colunas com intervalo de tempo expresso em minutos, os valores são divididos pelo número de minutos convertidos em horas.

    Exemplo de Uso:
    >>> df_convertido = converte_mm_por_h(df_dados)
    """
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
            # Pegando a quantidade de hroas
            horas = int(element.split('_')[-2])
            # Alterando o dataframe
            df[element] = df[element]/horas
        else:
            # Pegando a quantidade de horas também
            minutos_h = int(element.split('_')[-2])/60
            # Dividindo na equação
            df[element] = df[element]/minutos_h
    
    return df

def encontra_chuvas_mais_fortes(df, coluna_tempo, data_inicio=None, data_fim=None, quantidade_eventos=10, id_estacao=None, df_latitudes= None):
    """
    Encontra as chuvas mais fortes em um DataFrame de dados meteorológicos e também adiciona informações de latitude.

    Parameters:
    - df (DataFrame): DataFrame contendo os dados meteorológicos.
    - coluna_tempo (str): Nome da coluna usada para ordenar os eventos (por exemplo, 'acumulado_chuva_1_h').
    - data_inicio (str, opcional): Data de início do período de busca (formato 'YYYY-MM-DD').
    - data_fim (str, opcional): Data de término do período de busca (formato 'YYYY-MM-DD').
    - quantidade_eventos (int, opcional): Número de eventos a serem retornados (padrão é 10).
    - id_estacao (int, opcional): ID da estação meteorológica a ser filtrada.
    - df_latitudes (DataFrame, opcional): DataFrame contendo informações de latitude e longitude.

    Returns:
    - tuple: Uma tupla contendo:
        * Lista de identificadores dos eventos de chuva mais forte.
        * DataFrame contendo os dados dos eventos de chuva mais forte.
        * Dicionário contendo informações sobre cada evento de chuva mais forte.

    Documentation:
    Esta função recebe um DataFrame contendo dados meteorológicos e encontra as chuvas mais fortes com base em uma coluna de tempo especificada.
    É possível filtrar os eventos por período de tempo e/ou estação meteorológica.
    A função retorna uma lista com os identificadores dos eventos de chuva mais forte, um DataFrame com os dados desses eventos e um dicionário com informações sobre cada evento.
    Também adiciona informações de latitude e longitude aos dados dos eventos.

    Example:
    >>> eventos, df_eventos, dados_ranking = encontra_chuvas_mais_fortes_com_latitudes(df_meteorologia, 'acumulado_chuva_1_h', data_inicio='2023-01-01', data_fim='2023-12-31', quantidade_eventos=5, id_estacao=1, df_latitudes=df_latitudes)
    """
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
    total_iteracoes = len(chuvas_fortes)

    for iter, evento_chuvoso in enumerate(chuvas_fortes):
        df_filtrado = df_eventos[df_eventos["evento_chuvoso"] == evento_chuvoso]
        
        # Ordenando o DataFrame por 'data_hora' em ordem ascendente
        df_filtrado = df_filtrado.sort_values(by='data_hora', ascending=True)
        
        # Pegando a data de início do evento
        data_inicio_chuva = df_filtrado['data_hora'].iloc[0]
        
        # Pegando a data de término do evento
        data_fim_chuva = df_filtrado['data_hora'].iloc[-1]
        
        # Ordenando o DataFrame por 'acumulado_chuva_1_h' em ordem descendente
        df_filtrado = df_filtrado.sort_values(by='acumulado_chuva_1_h', ascending=False)
        
        # Pegando a maior quantidade de chuva acumulada em 1 hora durante o evento
        maior_chuva_evento = df_filtrado["acumulado_chuva_1_h"].iloc[0]
        
        # Adicionando o id específico
        id_estacao_especifica = df_filtrado["id_estacao"].iloc[0]

        # Size
        size_point = max(10, 100 - int(iter / total_iteracoes * 90))
        
        # Adicionando informações de latitude e longitude
        if df_latitudes is not None:
            latitude = df_latitudes[df_latitudes['id_estacao'] == id_estacao_especifica]['latitude'].iloc[0]
            longitude = df_latitudes[df_latitudes['id_estacao'] == id_estacao_especifica]['longitude'].iloc[0]
        else:
            latitude = None
            longitude = None

        # Convertendo as strings de data para objetos datetime
        data_inicio_chuva = datetime.strptime(data_inicio_chuva, "%Y-%m-%d %H:%M:%S")
        data_fim_chuva = datetime.strptime(data_fim_chuva, "%Y-%m-%d %H:%M:%S")

        # Calculando a duração da chuva em minutos e horas
        duracao_chuva = data_fim_chuva - data_inicio_chuva
        duracao_minutos = duracao_chuva.total_seconds() / 60
        duracao_horas = duracao_minutos / 60

        # Armazenando os resultados no dicionário dados_ranking
        dados_ranking[f"{evento_chuvoso}"] = [data_inicio_chuva, data_fim_chuva, maior_chuva_evento, id_estacao_especifica, size_point, latitude, longitude, duracao_minutos, duracao_horas]
   
    df_dados_ranking = pd.DataFrame.from_dict(dados_ranking, orient='index')

    df_dados_ranking= df_dados_ranking.rename(columns={
    0: "data_inicio_chuva",
    1: "data_fim_chuva",
    2: "maior_chuva_evento",
    3: "id_estacao_especifica",
    4: "size_point",
    5: "latitude",
    6: "longitude",
    7: "duracao_minutos",
    8: "duracao_horas"
})
    return chuvas_fortes, df_eventos, df_dados_ranking