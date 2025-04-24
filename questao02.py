import pandas as pd
import matplotlib.pyplot as plt

# Criando o DataFrame com os dados fornecidos
dados = pd.DataFrame({
    'Setor': [
        'TI', 'RH', 'TI', 'Financeiro', 'RH', 'TI', 'Financeiro', 'Financeiro', 'RH', 'TI',
        'RH', 'Financeiro', 'TI', 'TI', 'RH', 'RH', 'TI', 'Financeiro', 'RH', 'TI',
        'TI', 'Financeiro', 'Financeiro', 'TI', 'RH', 'RH', 'TI', 'TI', 'Financeiro', 'RH'
    ],
    'Escolaridade': [
        'Superior', 'Médio', 'Superior', 'Superior', 'Médio', 'Pós', 'Superior', 'Pós', 'Médio', 'Superior',
        'Médio', 'Superior', 'Pós', 'Médio', 'Médio', 'Superior', 'Pós', 'Médio', 'Superior', 'Superior',
        'Médio', 'Pós', 'Médio', 'Pós', 'Médio', 'Superior', 'Pós', 'Superior', 'Superior', 'Médio'
    ],
    'Tempo_Deslocamento': [
        15, 20, 25, 10, 35, 50, 45, 30, 60, 90,
        15, 20, 22, 18, 80, 12, 16, 75, 28, 33,
        55, 60, 100, 120, 8, 7, 20, 18, 14, 11
    ]
})

# Contar a quantidade de cada nível de escolaridade
escolaridade_counts = dados['Escolaridade'].value_counts()

# Criar o gráfico de pizza
escolaridade_counts.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90,
    figsize=(6, 6)
)

# Título e ajustes visuais
plt.title('Distribuição dos Níveis de Escolaridade dos Funcionários')
plt.ylabel('')  # Remove o rótulo do eixo y
plt.show()