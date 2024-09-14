import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime


st.set_page_config(
    layout="wide",
    page_title="spotify song"
)

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0) # passar o indice da coluna onde se encontra os dados
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year] #verifica se a data valida do contrato e maior ou igual data do ano do dia de hj
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False) #ordena lista pelo valor entre aspas
    st.session_state["data"] = df_data

st.markdown("# FIFA23 OFFICIAL DATASET!")
st.sidebar.markdown("Desenvolvido por [Yago Antunes Jorge](http://wa.me/5516991436958)", "https://www.kaggle.com/datasets")

btn = st.link_button("Acesse os dados no Kaggle") #definei um botao com o nome dentro de ()

st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)
