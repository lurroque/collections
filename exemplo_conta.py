from abc import ABCMeta, abstractmethod


class Conta(metaclass=ABCMeta):
    def __init__(
        self,
        codigo,
    ):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f">>Codigo: {self._codigo} | Saldo: {self._saldo}<<"

    # Método abstrato
    # As classes que herdarem da classe Conta,
    # obrigatoriamente precisarão reescrever esse método
    # Importar da classe abc, o ABCMeta e abstractmethod
    # Se o método não for reescrito, ocorrerá um:
    # TypeError: Can't instantiate abstract class Conta
    # with abstract method passa_o_mes
    @abstractmethod
    def passa_o_mes(self):
        pass


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaInvestimento(Conta):
    pass


###########################################################################


# Igualdade e o __eq__ junto de listas
# Ao trabalhar com listas que dependem da condição de igualdade,
# é necessário implementar um método fará essa comparação.
# São comprados atributos escolhidos
#
class ContaSalario(object):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    # Definindo método que compara igualdade
    # entre dois objetos
    # També é possível verificar o tipo do outro
    # objeto que será comparado
    def __eq__(self, outro_objeto):
        if type(outro_objeto) != ContaSalario:
            return False
        return (
            self._codigo == outro_objeto._codigo
            and self._saldo == outro_objeto._saldo
        )

    # utilizando magic method __lt__ (less then)
    # que permite que operadores de comparação
    # sejam usados para comprar objetos (< > ==)
    def __lt__(self, outro_objeto):
        return self._saldo < outro_objeto._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f">>Codigo: {self._codigo} | Saldo: {self._saldo}<<"
