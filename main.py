from exemplo_conta import (
    Conta,
    ContaCorrente,
    ContaPoupanca,
    ContaInvestimento,
    ContaSalario
)

# Um objeto só é instanciado se o seu construtor for chamado

# Se há necessidade de usar uma estrutura em que as posições
# são mais importantes, é nessário trabalhar com outro tipo de dado.
# Tupla
# OBS: Tuplas são imutáveis
# É possível apenas acessar seus valores
# t[0]
t = ("Roque", 30, 1990)


# Variação funcional
# O Objeto original não é alterado
# é possível atribuir esse objetos a novas variáveis,
# executar operações.
# E por fim, devolver um novo objeto a partir das operações realizadas.
conta_roque = (15, 100)


def deposita(conta):
    novo_saldo = conta_roque[1] + 100
    codigo = conta_roque[0]
    return (codigo, novo_saldo)


# valor = deposita(conta_roque)
# print(conta_roque)
# print(valor)


# Polimorfismo, Herança e Duck typing
conta_3 = ContaCorrente(3)
conta_3.deposita(1000)
conta_3.passa_o_mes()

conta_4 = ContaPoupanca(4)
conta_4.deposita(1000)
conta_4.passa_o_mes()

contas = [conta_3, conta_4]
# Não importa se na lista exista uma conta corrente
# ou uma conta poupança.
# Interessa que elas tenha o método passa_o_mes,
# essa característica é chamada de duck typing
for conta in contas:
    conta.passa_o_mes()
    print(conta)

conta_5 = ContaSalario(89)
conta_6 = ContaSalario(89)
print(conta_5 == conta_6)
