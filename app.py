import streamlit as st
import pandas as pd
import plotly.express as px

# Título do app
st.title("Dashboard ENEM - Análise das Notas (Amostra)")
st.write("Use os botões abaixo para visualizar os gráficos")

# Carregar os dados com cache
@st.cache_data
def load_data():
    df = pd.read_csv('dados/enem_amostra.csv', sep=',')
    return df

df = load_data()

# Filtro: participantes presentes nos dois dias
df_validos = df[(df['TP_PRESENCA_D1'] == 1) & (df['TP_PRESENCA_D2'] == 1)]

# Checkbox para histograma
if st.checkbox("Mostrar Histograma de Notas de Matemática"):
    fig = px.histogram(df_validos, x='NU_NOTA_MT', nbins=30,
                       title='Distribuição das Notas de Matemática')
    st.plotly_chart(fig)

# Checkbox para gráfico de dispersão
if st.checkbox("Mostrar Gráfico de Dispersão (Humanas vs Exatas)"):
    fig2 = px.scatter(df_validos, x='NU_NOTA_CH', y='NU_NOTA_CN',
                      color='TP_SEXO',
                      title='Relação entre Notas de Humanas e Exatas por Sexo')
    st.plotly_chart(fig2)
