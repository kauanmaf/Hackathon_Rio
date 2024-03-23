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