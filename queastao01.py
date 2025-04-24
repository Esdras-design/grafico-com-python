import pandas as pd
import matplotlib.pyplot as plt

# Seu DataFrame
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


contagem_setores = dados['Setor'].value_counts()


contagem_setores.plot(kind='bar')

plt.title('Quantidade de Funcionários por Setor')
plt.xlabel('Setor')
plt.ylabel('Quantidade')


plt.show()