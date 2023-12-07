# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:07:51 2023

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

db1 = sel(db, "Tipo de encontro", "cd_sigla_antibiotico")

# Contagem dos valores de Categoria_Y para cada valor único em Categoria_X
contagem = db1.groupby('cd_sigla_microorganismo')['cd_sigla_antibiotico'].value_counts().unstack().fillna(0)

# Plotando o gráfico de barras com Plotly
fig = go.Figure()

for categoria_y in contagem.columns:
    fig.add_trace(go.Bar(x=contagem.index, y=contagem[categoria_y], name=categoria_y))

# Adicionando título e rótulos aos eixos
fig.update_layout(title='Contagem de Exames por Bactéria',
                  xaxis_title='Tipos de Bactéria',
                  yaxis_title='Contagem de Exames',
                  barmode='stack')


# Definindo a escala do eixo y para uma menor
fig.update_layout(yaxis=dict(range=[0, 100]))  # Substitua [0, 100] pelo intervalo desejado

# Mostrando o gráfico no Streamlit
st.plotly_chart(fig)
