import basedosdados as bd

project_id = 'hackathon-fgv-417718'
queries = [
   #  "SELECT * FROM datario.dados_mestres.bairro;",
   #  "SELECT * FROM datario.adm_central_atendimento_1746.chamado;",
   #  "SELECT * FROM rj-rioaguas.dados_mestres.sub_bacias;",
   #  "SELECT * FROM rj-rioaguas.saneamento_drenagem.nivel_lamina_agua_via;",
    "SELECT * FROM rj-rioaguas.saneamento_drenagem.nivel_reservatorio;",
    "SELECT * FROM rj-rioaguas.saneamento_drenagem.ponto_supervisionado_alagamento;",
    "SELECT * FROM rj-cor.dados_mestres.h3_grid_res8;",
    "SELECT * FROM rj-cor.clima_pluviometro.estacoes_alertario;",
    "SELECT * FROM rj-cor.clima_pluviometro.estacoes_inea;",
    "SELECT * FROM rj-cor.clima_pluviometro.estacoes_cemaden;",
    "SELECT * FROM rj-cor.clima_pluviometro.estacoes_websirene;",
    "SELECT * FROM rj-cor.clima_pluviometro.taxa_precipitacao_alertario_5min;",
    "SELECT * FROM rj-cor.clima_pluviometro.taxa_precipitacao_inea;",
    "SELECT * FROM rj-cor.clima_pluviometro.taxa_precipitacao_cemaden;",
    "SELECT * FROM rj-cor.clima_pluviometro.taxa_precipitacao_websirene;",
    "SELECT * FROM rj-cor.clima_fluviometro.lamina_agua_inea;",
    "SELECT * FROM rj-cor.adm_cor_comando.ocorrencias;",
    "SELECT * FROM rj-cor.adm_cor_comando.procedimento_operacional_padrao;",
    "SELECT * FROM rj-cor.clima_radar.taxa_precipitacao_guaratiba;"
]

for query in queries:
    # Extract the table name from the query
    table_name = query.split('.')[-1].split()[0].rstrip(';')
    # Execute the query
    df = bd.read_sql(query, billing_project_id=project_id)
    # Save the DataFrame to a CSV file with the table name
    df.to_csv(f"database_csv/{table_name}.csv", index=False)
 