from reading_tables import *

# Como criar um ranking de chuvas?
print(cor_tx_precip_alerta_rio)

# Filtrando o dataset para os dias nos quais houveram chuvas
cor_tx_precip_alerta_rio = cor_tx_precip_alerta_rio[(cor_tx_precip_alerta_rio["acumulado_chuva_24h"]>0)]

# Ordenando os dados por data
cor_tx_precip_alerta_rio = cor_tx_precip_alerta_rio.sort_values(by='data_medicao', ascending=False)

# # Transformando os dados em mm/h

colunas_acumulado_chuva = ['acumulado_chuva_5min', 'acumulado_chuva_10min', 'acumulado_chuva_15min',
                           'acumulado_chuva_30min', 'acumulado_chuva_1h', 'acumulado_chuva_2h',
                           'acumulado_chuva_3h', 'acumulado_chuva_4h', 'acumulado_chuva_6h',
                           'acumulado_chuva_12h', 'acumulado_chuva_24h']

# Converter os acumulados de chuva para mm/h
for coluna in colunas_acumulado_chuva:
    # Extrair o período de tempo da coluna
    tempo_str = coluna.split('_')[2]
    if tempo_str[-3:] == "min":
        tempo = int(tempo_str[:-3]) / 60
    else:
        tempo = int(tempo_str[:-1])
    
    # Converter para mm/h
    cor_tx_precip_alerta_rio[coluna + '_mmh'] = cor_tx_precip_alerta_rio[coluna] / tempo


cor_tx_precip_alerta_rio['data_medicao'] = pd.to_datetime(cor_tx_precip_alerta_rio['data_medicao'])
print(cor_tx_precip_alerta_rio.shape)

dias_unicos = pd.unique(cor_tx_precip_alerta_rio['data_medicao'].dt.date)
print(len(dias_unicos))
