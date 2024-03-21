import basedosdados as bd

project_id = 'hackathon-fgv-417718'
queries = [
   #  "SELECT * FROM datario.dados_mestres.bairro;",
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
 

table_name = "chamado_2.csv"
    # Execute the query
query = """SELECT *
FROM `hackathon-fgv-417718.datario.1746_chamado`
WHERE tipo IN (
    'Remoção Programada', 
    'Desmoronamento', 
    'Geotecnia', 
    'Comlurb - Coleta Seletiva Sul', 
    'Escola',
    'Estabelecimentos e Serviços de Saúde',
    'Comlurb - Coleta Seletiva Oeste',
    'Danos ao meio ambiente',
    'Limpeza',
    'Acidentes',
    'Esgoto',
    'Poluição',
    'Fiscalização de obras',
    'Informação Não Encontrada - SMTR',
    'Programas Habitacionais - SMH',
    'Ouvidoria - CLF',
    'Engenharia de tráfego',
    'Atendimento ao cidadão',
    'BRT (corredor expresso de ônibus)',
    'Engenharia Sanitária',
    'Obras sem licença',
    'Diversos - GM',
    '2966',
    'Aplicativos',
    'Postura Municipal',
    'Manutenção de vias especiais',
    'Drenagem ou Esgoto',
    'Vetores',
    'Comlurb - Queimada',
    'Arborização',
    'Auxílio à população',
    'Documentos',
    'Patrimônio Municipal - Enfiteuse ou Aforamento',
    'Solicitação de obras',
    'Ouvidoria - Cidade das Artes',
    'Licença Ambiental',
    'Defesa civil',
    'Arboviroses',
    'Processos PGM',
    'Dengue',
    'Ônibus',
    'Remoção Gratuita',
    'Parques',
    'Programas Sociais',
    'Praia',
    'Vias públicas',
    'Manejo Arbóreo',
    'Zoonoses',
    'Auxílio',
    'Evento',
    'Planejamento',
    'Alagamento',
    'Drenagem e Saneamento',
    'Sinalização Gráfica',
    'Comlurb - Vetores',
    'Atendimento Social',
    'MEIO AMBIENTE',
    'Informação Não Encontrada',
    'Crimes',
    'Multas',
    'Vigilância sanitária',
    'Dívida Ativa',
    'Iluminação Pública',
    'Pavimentação'
);
"""

df = bd.read_sql(query, billing_project_id=project_id)
    # Save the DataFrame to a CSV file with the table name
df.to_csv(f"database_csv/{table_name}.csv", index=False)
 