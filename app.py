import streamlit as st
import pandas as pd
import plotly.express as px

# Título do app
st.title("Dashboard ENEM - Análise das Notas (Amostra)")
st.write("Use os checkboxes abaixo para visualizar os gráficos")

# Leitura do conjunto de dados
@st.cache_data
def load_data():
    return pd.read_csv('dados/enem_amostra.csv')

df = load_data()

# Filtro: apenas quem esteve presente nos dois dias
df_validos = df[(df['TP_PRESENCA_D1'] == 1) & (df['TP_PRESENCA_D2'] == 1)]

# Mostrar amostra da base
if st.checkbox("Visualizar primeiros dados"):
    st.dataframe(df.head())

# Histograma de notas de matemática
if st.checkbox("Histograma de Notas de Matemática"):
    fig = px.histogram(df_validos, x='NU_NOTA_MT', nbins=30,
                       title='Distribuição das Notas de Matemática')
    st.plotly_chart(fig)

# Gráfico de dispersão: CH x CN
if st.checkbox("Gráfico de Dispersão: Humanas vs. Ciências da Natureza"):
    fig = px.scatter(df_validos, x='NU_NOTA_CH', y='NU_NOTA_CN',
                     color='TP_SEXO',
                     title='Notas de Humanas vs. Ciências da Natureza por Sexo')
    st.plotly_chart(fig)
import streamlit as st
import pandas as pd
import plotly.express as px

# Supondo que você já tenha uma função para carregar os dados
@st.cache_data
def load_data():
    df = pd.read_csv('dados/enem_amostra.csv')  # ajuste o caminho conforme seu projeto
    return df

df = load_data()

st.title("Dashboard ENEM - Análise das Notas (Amostra)")
st.write("Use as opções abaixo para visualizar os gráficos:")

# Caixas de seleção para escolher o gráfico
show_hist = st.checkbox("Mostrar Histograma")
show_scatter = st.checkbox("Mostrar Gráfico de Dispersão")

if show_hist:
    fig_hist = px.histogram(df, x='NU_NOTA_MT', nbins=30, title='Histograma das Notas de Matemática')
    st.plotly_chart(fig_hist)

if show_scatter:
    fig_scatter = px.scatter(df, x='NU_NOTA_CN', y='NU_NOTA_CH',
                             title='Dispersão: Ciências da Natureza x Ciências Humanas',
                             labels={'NU_NOTA_CN': 'Nota Ciências da Natureza', 'NU_NOTA_CH': 'Nota Ciências Humanas'})
    st.plotly_chart(fig_scatter)
