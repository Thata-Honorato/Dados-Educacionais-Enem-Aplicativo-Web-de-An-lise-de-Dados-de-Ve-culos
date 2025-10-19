# Sprint 5 – Aplicativo Web de Análise de Dados de Veículos

## Descrição do Projeto

Neste projeto, meu objetivo foi praticar tarefas comuns de engenharia de software para aprimorar minhas habilidades em análise de dados e desenvolvimento de aplicações web. Trabalhei na criação de um **aplicativo web interativo** que me permitiu explorar visualmente os dados e gerar insights de forma prática.  

O foco do projeto foi:

- Criar e gerenciar ambientes virtuais em Python.  
- Desenvolver um aplicativo web usando **Streamlit**.  
- Implementar gráficos interativos com **Plotly Express**.  
- Implantar o aplicativo na nuvem usando **Render**.  

O conjunto de dados utilizado contém anúncios de vendas de carros (`vehicles_us.csv`). No entanto, o aplicativo poderia funcionar com qualquer CSV que eu escolhesse para análise.

---

## Funcionalidades do Aplicativo Web

No aplicativo que desenvolvi, implementei:

1. Um **cabeçalho** para apresentar o projeto ao usuário.  
2. Um **histograma interativo**, gerado ao clicar em um botão ou selecionar uma caixa de seleção, para analisar distribuições de variáveis como odômetro, preço ou ano do veículo.  
3. Um **gráfico de dispersão interativo**, também acionado por botão ou caixa de seleção, permitindo observar relações entre diferentes variáveis do dataset.  
4. Integração com **Plotly Express** para gráficos interativos e responsivos.  
5. Um layout simples, funcional e fácil de usar.

Exemplo de trecho de código utilizado:

```python
import pandas as pd
import plotly.express as px
import streamlit as st

# Leitura do dataset
car_data = pd.read_csv('vehicles_us.csv')

# Criar um botão para histograma
hist_button = st.button('Criar histograma')
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Criar um botão para gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')
if scatter_button:
    st.write('Criando gráfico de dispersão para análise exploratória')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
