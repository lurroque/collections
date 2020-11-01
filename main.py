from listas_objetos import ContaCorrente

# Um objeto só é instanciado se o seu construtor for chamado
conta_1 = ContaCorrente(15)
conta_1.deposita(100)
conta_2 = ContaCorrente(14)
conta_2.deposita(200)

# Se há necessidade de usar uma estrutura em que as posições
# são mais importantes, é nessário trabalhar com outro tipo de dado.
# Tupla
# OBS: Tuplas são imutáveis
# É possível apenas acessar seus valores
# t[0]

t = ("Roque", 30, 1990)

print(t)
