import streamlit as st
import pandas as pd

db = pd.read_csv('C:/Users/pedro/Downloads/dadoslimpos.csv', sep=',')


st.header("Painel de Busca")


st.subheader('Tabela interativa de dados', divider='rainbow')

def sel(db,nome,col):
    cat = st.selectbox(
        nome,
        ['Todos'] + list(db[col].unique())
    )

    if cat != 'Todos':

        db = db[db[col] == cat]
        
    return db

db1 = sel(db,'Tipo de encontro','ds_tipo_encontro')

db1 = sel(db1,'Unidade da coleta','ds_unidade_coleta')

db1 = sel(db1,'Prédio da coleta','ds_predio_coleta')

db1 = sel(db1,'Ala da coleta','ds_ala_coleta')

db1 = sel(db1,'Tipo de exame','ds_exame_millennium')

db1 = sel(db1,'Tipo de material','ds_material_millennium')

 
 
st.dataframe(db1)

res = len(db1.index)

st.write('Resultados da filtragem: ',res)
    
