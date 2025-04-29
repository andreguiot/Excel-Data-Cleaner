import pandas as pd
import matplotlib.pyplot as plt

# 1. Ler a planilha
df = pd.read_excel('dados/dados_brutos.xlsx')

# 2. Limpeza de dados
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df.dropna(how='all', inplace=True)

def corrigir_idade(valor):
    try:
        return int(valor)
    except:
        return None

if 'idade' in df.columns:
    df['idade'] = df['idade'].apply(corrigir_idade)

if 'data_cadastro' in df.columns:
    df['data_cadastro'] = pd.to_datetime(df['data_cadastro'], errors='coerce')

if 'email' in df.columns:
    df['email'] = df['email'].fillna('sem_email@dominio.com')

df.fillna('-', inplace=True)

# 3. Salvar dados tratados
df.to_excel('dados/dados_tratados.xlsx', index=False)
print('Limpeza concluída. Planilha salva em dados_tratados.xlsx.')

# 4. Criar gráfico simples: número de cadastros por cidade
if 'cidade' in df.columns:
    contagem_cidades = df['cidade'].value_counts()

    plt.figure(figsize=(8,6))
    contagem_cidades.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Número de Cadastros por Cidade')
    plt.xlabel('Cidade')
    plt.ylabel('Quantidade de Cadastros')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('dados/grafico_cadastros_por_cidade.png')
    print('Gráfico gerado em dados/grafico_cadastros_por_cidade.png')