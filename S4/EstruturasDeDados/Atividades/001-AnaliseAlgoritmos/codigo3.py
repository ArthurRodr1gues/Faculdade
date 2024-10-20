import matplotlib.pyplot as plt
import numpy as np

# Limites definidos
limites = [3, 10, 100, 10000]  # O primeiro limite foi ajustado para 10
num_pontos = 10  # Número de pontos para cada gráfico

# Cria uma figura com 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs = axs.flatten()  # Facilita o acesso aos subplots

# Configurações dos gráficos
for i, lim in enumerate(limites):
    n = np.linspace(1, lim, num_pontos)  # Gera valores de n de 1 até o limite
    
    # Complexidades assintóticas
    O1 = np.ones_like(n)
    On = n
    On2 = n**2
    Ologn = np.log(n)
    Onlogn = n * np.log(n)

    # Plota os gráficos
    axs[i].plot(n, O1, label="O(1)", marker='o')
    axs[i].plot(n, On2, label="O(n^2)", marker='^')
    axs[i].plot(n, On, label="O(n)", marker='s')
    axs[i].plot(n, Ologn, label="O(log(n))", marker='x')
    axs[i].plot(n, Onlogn, label="O(n log(n))", marker='d')

    axs[i].set_xlabel("Tamanho da entrada")
    axs[i].set_ylabel("Número de Operações")
    axs[i].set_title(f"Comparação de Complexidade Assintótica (n até {lim})")
    axs[i].legend()
    axs[i].grid(True)
    axs[i].set_xlim(1, lim)  # Define os limites do eixo x
    axs[i].set_ylim(0, np.max(On2) * 1.1)  # Limites do eixo y

# Ajuste o layout
plt.tight_layout()
plt.show()
