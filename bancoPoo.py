from abc import ABC, abstractmethod

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico

    @property
    def saldo(self):
        return self.saldo
    @property
    def numero(self):
        return self.numero
    @property
    def agencia(self):
        return self.agencia
    @property
    def cliente(self):
        return self.cliente
    @property
    def historico(self):
        return self.historico

    @classmethod
    def novaConta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        saldo = self.saldo

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True

        else:
            print("Operação falhou! O valor informado é inválido.")

        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False

        return True
    

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico):
        super().__init__(saldo, numero, agencia, cliente, historico, limite=500, limite_saques=3)


class Historico:
    def __init__(self):
        self.transacoes = []

    @property
    def transacoes(self):
        return self.transacoes

    def adicionarTransacao(self, transacao):
        self.transacoes.append(transacao)


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    def registrar(self, conta):
        pass


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    @property
    def endreco(self):
        return self.endereco
    
    @property
    def contas(self):
        return self.contas
    
    def realizarTransacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionarConta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, dataNascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.dataNascimento = dataNascimento


def exibirMenu():
    menu = """
[d] Deposito
[s] Sacar
[e] Extrato
[u] Adicionar Usuario
[c] Nova Conta
[l] Listar Contas
[q] Sair
"""
    print(menu)

def main():
    cont = True
    exibirMenu();
    while cont:
        opt = input(">>>")
        cont = opcao(opt)

def depositar():
    print("Depositar")

def sacar(): 
    print("Sacar")

def exibirExtrato():
    print("Ext")

def addUsuario():
    print("Add U")

def addConta():
    print("Add conta")

def listarContas():
    print("Listar")

def opcao(opt):
    if opt == "d":
        depositar()
        return True
    elif opt == "s":
        sacar()
        return True
    elif opt == "e":
        exibirExtrato()
        return True
    elif opt == "u":
        addUsuario()
        return True
    elif opt == "c":
        addConta()
        return True 
    elif opt == "l":
        listarContas()
        return True
    elif opt == "q":
        return False
    else:
        return True

main()
