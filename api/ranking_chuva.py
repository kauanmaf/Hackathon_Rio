from reading_tables import *
from utils import *

# Lendo o csv
datario_tx_precip_alerta_rio = pd.read_csv("database_csv/taxa_precipitacao_alertario.csv")

# Criando uma coluna com o horário preciso da medição
datario_tx_precip_alerta_rio["data_hora"] = datario_tx_precip_alerta_rio["data_particao"] + ' ' + datario_tx_precip_alerta_rio["data_particao"]

# Converter para datetime algumas das colunas
datario_tx_precip_alerta_rio['data_hora'] = pd.to_datetime(datario_tx_precip_alerta_rio['data_hora'])
datario_tx_precip_alerta_rio['data_particao'] = pd.to_datetime(datario_tx_precip_alerta_rio['data_particao'])

#   Ordenando por data o dataframe
datario_tx_precip_alerta_rio = datario_tx_precip_alerta_rio.sort_values(by='data_hora', ascending=True)

# Preenchendo valores NaN com 0 nas colunas especificadas
colunas_chuva = ['acumulado_chuva_15_min', 'acumulado_chuva_1_h', 'acumulado_chuva_4_h', 'acumulado_chuva_24_h']
datario_tx_precip_alerta_rio[colunas_chuva] = datario_tx_precip_alerta_rio[colunas_chuva].fillna(0)
datario_tx_precip_alerta_rio[colunas_chuva] = datario_tx_precip_alerta_rio[colunas_chuva].astype(float)

# Utilizando a função para criar as colunas que desejamos, com base na soma móvel.
datario_tx_precip_alerta_rio_red = datario_tx_precip_alerta_rio.loc[datario_tx_precip_alerta_rio['data_particao'].dt.year >= 2016].copy()


datario_tx_precip_alerta_rio_red = processamento_acumulado_chuva(datario_tx_precip_alerta_rio_red)

datario_tx_precip_alerta_rio_red = ordenar_colunas(datario_tx_precip_alerta_rio_red)

datario_tx_precip_alerta_rio_red = converte_mm_por_h(datario_tx_precip_alerta_rio_red)

datario_tx_precip_alerta_rio_red = encontra_chuvas_mais_fortes()