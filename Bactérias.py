# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:06:51 2023

@author: bitan
"""

"""
Created on Fri Dec 1 10:51:16 2023
@author: bitan
"""

import plotly.graph_objects as go
import streamlit as st
import pandas as pd

db = pd.read_csv("C:/Users/bitan/Desktop/PBL P/dadoslimpostempo.csv", sep=',')

st.header("Painel de Busca")
st.subheader('Tabela interativa de dados', divider='rainbow')

def sel(db, nome, col):
    cat = st.selectbox(
        nome,
        ['Todos'] + list(db[col].unique())
    )

    if cat != 'Todos':
        db = db[db[col] == cat]
        
    return db

db['Índice'] = db.index
db['dh_admissao_paciente'] = pd.to_datetime(db['dh_admissao_paciente'])
dados_mensais = db.groupby([pd.Grouper(key="dh_admissao_paciente", freq='Y'), "cd_sigla_microorganismo"]).count()["Índice"]

# Plotando o gráfico de barras
fig = go.Figure()

for bacteria in db['cd_sigla_microorganismo'].unique():
    fig.add_trace(go.Bar(x=dados_mensais.index.get_level_values(0).unique(),
                         y=dados_mensais[dados_mensais.index.get_level_values(1) == bacteria],
                         name=bacteria))

# Adicionando título e rótulos aos eixos
fig.update_layout(title='Contagem de Bactérias por ano',
                  xaxis_title='Ano',
                  yaxis_title='Bactéria')

# Mostrando o gráfico
st.plotly_chart(fig)
