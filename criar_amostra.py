import pandas as pd

print("Lendo as primeiras 5000 linhas do arquivo...")

# Ajuste o separador se seu CSV usar outro (exemplo: ';' ou ',')
df = pd.read_csv('dados/Data_Base.csv', sep=';', nrows=5000)

print("Salvando a amostra em enem_amostra.csv...")

df.to_csv('dados/enem_amostra.csv', index=False)

print("Amostra criada com sucesso!")

