import streamlit as st


df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index # posso usar a função unique ao inves de valur_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[(df_data["Club"] == club)] # dataframe df_players vai ser todos onde a coluna "Club" é igual a club

players = df_players["Name"].value_counts().index # posso usar a função unique ao inves de valur_counts().index
player = st.sidebar.selectbox("Jogador", players) # define o sidebar com a variavel players que contem os valores 

player_stats = df_data[df_data["Name"]== player].iloc[0] # a variavel é o data frame quando no data frame coluna Name fo igual a opção selecionada no sidebar player e a função .iloc[0] primeiro indice para selecionar a linha inteira

st.image(player_stats['Photo']) # coloca a foto do jogador que foi selecionado anteriormente
st.title(player_stats['Name']) # coloca o nome do jogador

st.markdown(f'**Clube:** {player_stats["Club"]}')
st.markdown(f'**Positição:** {player_stats["Position"]}')

col1, col2, col3, cpl4 = st.columns(4)
col1.markdown(f'**Idade:** {player_stats["Age"]}')
col2.markdown(f'**Idade:** {player_stats["Height(cm.)"]/100}')
col3.markdown(f'**Idade:** {player_stats["Weight(lbs.)"]*0.453:.0f}') # :.2f para definir quantas casas depois da virgula
st.divider() # cria uma linha abaixo

st.subheader(f'Overall {player_stats["Overall"]}')
st.progress(int(player_stats["Overall"])) # barra deprogresso de 0 a 100padrao

col1, col2, col3, cpl4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")
