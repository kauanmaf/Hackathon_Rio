import pandas as pd
import numpy as np

# Dados Gerais
dg_bairros = pd.read_csv("database_csv/bairro.csv")
dg_sub_bacias = pd.read_csv("database_csv/sub_bacias.csv")
dg_grid = pd.read_csv("database_csv/h3_grid_res8.csv")

# # Dados de COR, 1746, e pontos supervisionados
cor_ocorrencias = pd.read_csv("database_csv/ocorrências.csv")
cor_pop = pd.read_csv("database_csv/procedimento_operacional_padrao.csv")
# datario_chamado_1746 = pd.read_csv("database_csv/chamado.csv")
ra_psalagamento = pd.read_csv("database_csv/ponto_supervisionado_alagamento.csv")

# # Dados Pluviométricos
cor_est_alerta_rio = pd.read_csv("database_csv/estacoes_alertario.csv")
cor_est_inea = pd.read_csv("database_csv/estacoes_inea.csv")
cor_est_cemaden = pd.read_csv("database_csv/estacoes_cemaden.csv")
cor_est_websirene = pd.read_csv("database_csv/estacoes_websirene.csv")

# cor_tx_precip_websirene = pd.read_csv("database_csv/taxa_precipitacao_websirene.csv")
cor_tx_precip_alerta_rio = pd.read_csv("database_csv/taxa_precipitacao_alertario_5min.csv")
cor_tx_precip_inea = pd.read_csv("database_csv/taxa_precipitacao_inea.csv")
cor_tx_precip_cemaden = pd.read_csv("database_csv/taxa_precipitacao_cemaden.csv")

# # Dados Fluviométricos e dados de reservtórios
ra_lam_inea = pd.read_csv("database_csv/lamina_agua_inea.csv")
ra_lam_via = pd.read_csv("database_csv/nivel_lamina_agua_via.csv")
ra_nivel_reservatorio = pd.read_csv("database_csv/nivel_reservatorio.csv")

# # Radares_metereológicos
# cor_tx_precip_guaratiba = pd.read_csv("database_csv/taxa_precipitacao_guaratiba.csv")