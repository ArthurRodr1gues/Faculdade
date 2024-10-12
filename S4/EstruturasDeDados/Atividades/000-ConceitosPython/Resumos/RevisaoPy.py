# Criação de Listas
minha_lista = [1, 2, 3, 4, 5]
outra_lista = list((6, 7, 8, 9, 10))

# Acesso a Elementos
print("Primeiro elemento:", minha_lista[0])  # Primeiro elemento: 1
print("Último elemento:", minha_lista[-1])  # Último elemento: 5

# Modificação de Listas
# Adicionar Elementos
minha_lista.append(6)
print("Após append:", minha_lista)  # Após append: [1, 2, 3, 4, 5, 6]

minha_lista.extend([7, 8])
print("Após extend:", minha_lista)  # Após extend: [1, 2, 3, 4, 5, 6, 7, 8]

minha_lista.insert(0, 0)
print("Após insert:", minha_lista)  # Após insert: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Remover Elementos
minha_lista.remove(0)
print("Após remove:", minha_lista)  # Após remove: [1, 2, 3, 4, 5, 6, 7, 8]

elemento_removido = minha_lista.pop(0)
print("Após pop:", minha_lista, "Elemento removido:", elemento_removido)  # Após pop: [2, 3, 4, 5, 6, 7, 8] Elemento removido: 1

minha_lista.clear()
print("Após clear:", minha_lista)  # Após clear: []

# Operações de Listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
nova_lista = lista1 + lista2
print("Concatenar listas:", nova_lista)  # Concatenar listas: [1, 2, 3, 4, 5, 6]

repetida_lista = lista1 * 3
print("Repetir lista:", repetida_lista)  # Repetir lista: [1, 2, 3, 1, 2, 3, 1, 2, 3]

print("Verificar existência do 2 em lista1:", 2 in lista1)  # Verificar existência do 2 em lista1: True

# Funções de Listas
print("Comprimento de lista1:", len(lista1))  # Comprimento de lista1: 3
print("Lista ordenada:", sorted(lista2, reverse=True))  # Lista ordenada: [6, 5, 4]
print("Soma dos elementos de lista1:", sum(lista1))  # Soma dos elementos de lista1: 6
print("Menor elemento de lista2:", min(lista2))  # Menor elemento de lista2: 4
print("Maior elemento de lista2:", max(lista2))  # Maior elemento de lista2: 6

# Métodos de Listas
lista3 = [1, 2, 2, 3, 4, 4, 4, 5]
print("Índice da primeira ocorrência do 4:", lista3.index(4))  # Índice da primeira ocorrência do 4: 4
print("Número de ocorrências do 4:", lista3.count(4))  # Número de ocorrências do 4: 3

lista3.sort()
print("Lista ordenada in-place:", lista3)  # Lista ordenada in-place: [1, 2, 2, 3, 4, 4, 4, 5]

lista3.reverse()
print("Lista invertida in-place:", lista3)  # Lista invertida in-place: [5, 4, 4, 4, 3, 2, 2, 1]

copia_lista3 = lista3.copy()
print("Cópia da lista3:", copia_lista3)  # Cópia da lista3: [5, 4, 4, 4, 3, 2, 2, 1]
