import matplotlib.pyplot as plt
import numpy as np

lim = 10000
n = np.arange(1, lim, lim/20)

# Complexidades assintóticas
O1 = np.ones_like(n)
On = n
On2 = n**2
Ologn = np.log(n)
Onlogn = n*np.log(n)

plt.plot(n, O1, label="O(1)", marker='o')
plt.plot(n, On2, label="O(n ^ 2)", marker='^')
plt.plot(n, On, label="O(n)", marker='s')
plt.plot(n, Ologn, label="O(log(n))", marker='x')
plt.plot(n, Onlogn, label="O(nlog(n))", marker='d')

plt.xlabel("Tamanho da entrada")
plt.ylabel("Número de Operações")
plt.title("Comparação de Complexidade Assintótica")
plt.legend()
plt.grid(True)
plt.show()
