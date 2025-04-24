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

# Criar o boxplot do tempo de deslocamento
plt.figure(figsize=(8, 6))
plt.boxplot(dados['Tempo_Deslocamento'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribuição do Tempo de Deslocamento ao Trabalho')
plt.ylabel('Tempo de Deslocamento (minutos)')
plt.grid(True)
plt.show()