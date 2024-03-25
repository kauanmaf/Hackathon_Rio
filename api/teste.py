import streamlit as st
import pandas as pd
import plotly.express as px

def plot_map(df, title):
    # Plotar os dados em um mapa
    fig = px.scatter_mapbox(df, 
                            lat="latitude", 
                            lon="longitude", 
                            color_discrete_sequence=['black'],
                            hover_name="estacao",
                            size_max = 30,
                            zoom=10)

    # Personalizar o layout do mapa
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(title=title,
                      margin={"r":0,"t":30,"l":0,"b":0})

    # Mostrar o mapa
    st.write(fig)

# Carregar os dados do CSV
cor_est_alerta_rio = pd.read_csv("api/database_csv/estacoes_alertario.csv")
cor_est_alerta_rio['cota'].fillna(0, inplace=True)
cor_est_inea = pd.read_csv("api/database_csv/estacoes_inea.csv")
cor_est_cemaden = pd.read_csv("api/database_csv/estacoes_cemaden.csv")
cor_est_websirene = pd.read_csv("api/database_csv/estacoes_websirene.csv")

# Plotar os mapas
plot_map(cor_est_alerta_rio, "Estações de Monitoramento Alerta Rio")
plot_map(cor_est_inea, "Estações de Monitoramento Inea")
plot_map(cor_est_websirene, "Estações de Monitoramento Websirene")
plot_map(cor_est_cemaden, "Estações de Monitoramento Cemaden")
