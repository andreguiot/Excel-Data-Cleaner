import matplotlib.pyplot as plt

# Dados fictícios
cidades = ['Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Porto Alegre', 'Curitiba']
quantidades = [120, 180, 90, 60, 80]

# Criar o gráfico
plt.figure(figsize=(8,6))
plt.bar(cidades, quantidades, color='skyblue', edgecolor='black')
plt.title('Número de Cadastros por Cidade', fontsize=16)
plt.xlabel('Cidade', fontsize=12)
plt.ylabel('Quantidade de Cadastros', fontsize=12)
plt.xticks(rotation=30)
plt.tight_layout()

# Salvar o gráfico como imagem
plt.savefig('grafico_exemplo_readme.png')