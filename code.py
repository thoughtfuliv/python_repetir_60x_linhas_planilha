# Instala a biblioteca pandas, se necessário
!pip install pandas

import pandas as pd

# Monta o Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Caminho para o arquivo Excel no Google Drive
caminho_arquivo = '/content/drive/MyDrive/TESTE PAT COLAB/PAT - TESTE.xlsx'

# Carrega a planilha Excel em um DataFrame do pandas
df = pd.read_excel(caminho_arquivo)

# Cria uma nova lista vazia para armazenar as linhas repetidas
linhas_repetidas = []

# Repete cada linha 60 vezes
for index, row in df.iterrows():
    for i in range(60):
        linhas_repetidas.append(row)

# Cria um novo DataFrame com as linhas repetidas
df_repetido = pd.DataFrame(linhas_repetidas)

# Caminho para salvar o arquivo repetido no Google Drive
caminho_salvar = '/content/drive/MyDrive/TESTE PAT COLAB/PAT - TESTE.xlsx'

# Salva o DataFrame repetido em um novo arquivo Excel
df_repetido.to_excel(caminho_salvar, index=False)

print("Planilha repetida e salva com sucesso!")
