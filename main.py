from listas_objetos import ContaCorrente

# Um objeto só é instanciado se o seu construtor for chamado
conta_1 = ContaCorrente(15)
conta_1.deposita(100)
conta_2 = ContaCorrente(14)
conta_2.deposita(200)

contas = [conta_1, conta_2, conta_1]
print(conta_1)
