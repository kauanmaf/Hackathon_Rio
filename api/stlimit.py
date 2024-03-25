import pandas as pd
import numpy as np
from utils import *
import streamlit as st

datario_tx_precip_alerta_rio = pd.read_csv("api/database_csv/taxa_precipitacao_alertario.csv")
cor_est_alerta_rio = pd.read_csv("api/database_csv/estacoes_alertario.csv")

# Criando uma coluna com o horário preciso da medição
datario_tx_precip_alerta_rio["data_hora"] = datario_tx_precip_alerta_rio["data_particao"] + ' ' + datario_tx_precip_alerta_rio["horario"]

# Converter para datetime
datario_tx_precip_alerta_rio['data_hora'] = pd.to_datetime(datario_tx_precip_alerta_rio['data_hora'])
datario_tx_precip_alerta_rio['data_particao'] = pd.to_datetime(datario_tx_precip_alerta_rio['data_particao'])


datario_tx_precip_alerta_rio = datario_tx_precip_alerta_rio.sort_values(by='data_hora', ascending=True)
datario_tx_precip_alerta_rio = datario_tx_precip_alerta_rio[~pd.isna(datario_tx_precip_alerta_rio["data_hora"])]

# Preencher valores NaN com 0 nas colunas especificadas
colunas_chuva = ['acumulado_chuva_15_min', 'acumulado_chuva_1_h', 'acumulado_chuva_4_h', 'acumulado_chuva_24_h']

datario_tx_precip_alerta_rio[colunas_chuva] = datario_tx_precip_alerta_rio[colunas_chuva].fillna(0)
datario_tx_precip_alerta_rio[colunas_chuva] = datario_tx_precip_alerta_rio[colunas_chuva].astype(float)

datario_tx_precip_alerta_rio_red = datario_tx_precip_alerta_rio.loc[datario_tx_precip_alerta_rio['data_particao'].dt.year >= 2016].copy()

# Supondo que 'datario_tx_precip_alerta_rio_red' seja o nome do seu DataFrame
# Substitua esse nome pelo nome real do seu DataFrame

# Calculando a próxima data usando shift()
datario_tx_precip_alerta_rio_red['proximo_data'] = datario_tx_precip_alerta_rio_red['data_particao'].shift(-1)

datario_tx_precip_alerta_rio_red = datario_tx_precip_alerta_rio_red.dropna(subset=['data_particao', 'proximo_data'])

# Calculando a diferença entre datas consecutivas em minutos
datario_tx_precip_alerta_rio_red['diferenca_minutos'] = (datario_tx_precip_alerta_rio_red['proximo_data'] - datario_tx_precip_alerta_rio_red['data_particao']).dt.total_seconds() / 60

# Convertendo para inteiros
datario_tx_precip_alerta_rio_red['diferenca_minutos'] = datario_tx_precip_alerta_rio_red['diferenca_minutos'].astype(int)

# Retirando linhas onde a diferença é 5 ou 10 minutos
datario_tx_precip_alerta_rio_red = datario_tx_precip_alerta_rio_red[(datario_tx_precip_alerta_rio_red['diferenca_minutos'] != 5) & (datario_tx_precip_alerta_rio_red['diferenca_minutos'] != 10)]

# Se desejar, você pode remover a coluna de diferença de minutos após filtrar as linhas
del datario_tx_precip_alerta_rio_red['diferenca_minutos']
del datario_tx_precip_alerta_rio_red['proximo_data']

datario_tx_precip_alerta_rio_red = processamento_acumulado_chuva(datario_tx_precip_alerta_rio_red)

datario_tx_precip_alerta_rio_red = ordenar_colunas(datario_tx_precip_alerta_rio_red)

datario_tx_precip_alerta_rio_red = converte_mm_por_h(datario_tx_precip_alerta_rio_red)

eventos_chuvosos, dados_eventos, df_result = encontra_chuvas_mais_fortes(datario_tx_precip_alerta_rio_red, 'acumulado_chuva_1_h', quantidade_eventos=10, df_latitudes=cor_est_alerta_rio)

# Criar um dicionário que mapeia os IDs das estações para os nomes das estações
mapa_estacoes = dict(zip(cor_est_alerta_rio['id_estacao'], cor_est_alerta_rio['estacao']))

# Função para obter o nome da estação com base no ID da estação
def obter_nome_estacao(id_estacao):
    return mapa_estacoes.get(id_estacao, "Estação Desconhecida")  # Retorna o nome da estação se existir no dicionário, caso contrário retorna "Estação Desconhecida"

# Adicionar a nova coluna 'nome' ao DataFrame df_result
df_result['nome'] = df_result['id_estacao_especifica'].map(obter_nome_estacao)

# Interface do Streamlit
st.title('Encontre as Chuvas Mais Fortes')
data_inicio = st.date_input('Data de Início')
data_fim = st.date_input('Data de Fim')

# Lista de opções para a coluna de tempo
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
coluna_tempo = st.selectbox('Selecione a coluna de tempo:', colunas_tempo)

# Botão para encontrar as chuvas mais fortes
if st.button('Encontrar Chuvas Mais Fortes'):
    # Chamada da função
    eventos_chuvosos, dados_eventos, df_result = encontra_chuvas_mais_fortes(datario_tx_precip_alerta_rio_red, 'acumulado_chuva_1_h', quantidade_eventos=10, df_latitudes=cor_est_alerta_rio)
    st.write(df_result)

