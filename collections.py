# Referência na Doc
# https://docs.python.org/3/tutorial/datastructures.html

idades = [21, 40, 19, 28, 20]

# Métodos referentes a lista

# Exibe o tamanho
len(idades)

# Acrescentando elementos no fim
idades.append(54)

# Percorrendo
for idade in idades:
    print(idade)

# Removendo um elemento
# Havendo mais de um deste elemento,apenas a primeira aparição é removida
idades.remove(40)

# Removendo todos os elementos
# idades.clear()

# Inserindo um elemento na posição desejada
idades.insert(0, 20)

# Inserindo vários elementos em uma lista(Passar um iterável como parâmetro)
idades.extend([5, 10, 15])

# List comprehension
# Tudo que está antes do for,
# é que será aplicado para cada item percorrido na lista
idades_no_ano_que_vem = [idade + 1 for idade in idades if idade >= 21]

# Percorrendo a lista pela posição e valor
for i in range(len(idades)):
    print(i, idades[i])
# ou
print(list(enumerate(idades)))

# Desempacotando(Unpacking) a tupla
for indice, idade in enumerate(idades):
    print(indice, "-", idade)

usuarios = [
    ("nome1", 33, 1988),
    ("nome2", 32, 1989),
    ("nome2", 31, 1990)
]

# Buscando um índice de uma tupla, percorrendo uma lista
# Percorrer exatamente o número de elementos que aparecem
# nas tuplas da lista
for nome, idade, nascimento in usuarios:
    print(nome, idade)

# Mais alguns tipos de geradores
# Ordenação crescente e decrescente sem alterar a lista original
print(idades)
print(sorted(idades, reverse=True))

# Ordenação alterando a lista original
idades.sort()
