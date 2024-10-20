import matplotlib.pyplot as plt
import numpy as np

# Definir o intervalo de n para valores grandes
lim_inferior = 10000
lim_superior = 20000
n = np.arange(lim_inferior, lim_superior, (lim_superior - lim_inferior) / 20)

# Definir diferentes intervalos de n para as outras funções para evitar sobreposição
n1 = np.arange(lim_inferior, lim_superior, (lim_superior - lim_inferior) / 20)
n3 = np.arange(lim_inferior + 2000, lim_superior + 2000, (lim_superior - lim_inferior) / 20)
n4 = np.arange(lim_inferior + 3000, lim_superior + 3000, (lim_superior - lim_inferior) / 20)
n5 = np.arange(lim_inferior + 4000, lim_superior + 4000, (lim_superior - lim_inferior) / 20)

# Definir as complexidades para cada intervalo de n
O1 = np.ones_like(n1)
On = n  # Corrigido, O(n) deve usar o vetor n
On2 = n3**2
Ologn = np.log(n4)
Onlogn = n5 * np.log(n5)

# Plotar as funções com marcadores diferentes
plt.plot(n3, On2, label="O(n^2)", marker='^')
plt.plot(n1, O1, label="O(1)", marker='o')
plt.plot(n, On, label="O(n)", marker='s')  # Aqui está a função O(n) corrigida
plt.plot(n4, Ologn, label="O(log(n))", marker='x')
plt.plot(n5, Onlogn, label="O(nlogn)", marker='d')

plt.xlabel("Tamanho da entrada")
plt.ylabel("Número de Operações")
plt.title("Comparação de Complexidade Assintótica (n de 10000 a 20000)")
plt.legend()
plt.grid(True)
plt.show()
