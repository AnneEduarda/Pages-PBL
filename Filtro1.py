import streamlit as st
import pandas as pd

db = pd.read_csv('C:/Users/pedro/Downloads/dadoslimpos.csv', sep=',')

st.header("Filtro")


st.subheader('Tabela interativa de dados', divider='rainbow')


cat = st.selectbox(
    "Tipo de encontro",
    ['Todos'] + list(db["ds_tipo_encontro"].unique())
)

if cat != 'Todos':

    db = db[db["ds_tipo_encontro"] == cat]
    
    


cat = st.selectbox(
    "Unidade da coleta",
    ['Todos'] + list(db["ds_unidade_coleta"].unique())
)

if cat != 'Todos':

    db = db[db["ds_unidade_coleta"] == cat]
    
    


cat = st.selectbox(
    "Prédio da coleta",
    ['Todos'] + list(db["ds_predio_coleta"].unique())
)

if cat != 'Todos':

    db = db[db["ds_predio_coleta"] == cat]
    
    


cat = st.selectbox(
    "Ala da coleta",
    ['Todos'] + list(db["ds_ala_coleta"].unique())
)

if cat != 'Todos':

    db = db[db["ds_ala_coleta"] == cat]



cat = st.selectbox(
    "Tipo de exame",
    ['Todos'] + list(db["ds_exame_millennium"].unique())
)

if cat != 'Todos':

    db = db[db["ds_exame_millennium"] == cat]
    
    
    
cat = st.selectbox(
    "Tipo de material",
    ['Todos'] + list(db["ds_material_millennium"].unique())
)

if cat != 'Todos':

    db = db[db["ds_material_millennium"] == cat]
    
    
st.dataframe(db)

res = len(db.index)

st.write('Resultados da filtragem: ',res)
