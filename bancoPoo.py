from abc import ABC, abstractmethod

usuarios = []
contas = []


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    @property
    def numero(self):
        return self._numero
    @property
    def agencia(self):
        return self._agencia
    @property
    def cliente(self):
        return self._cliente
    @property
    def historico(self):
        return self._historico

    @classmethod
    def novaConta(cls, numero, cliente):
        return cls(numero, cliente)

    def sacar(self, valor):
        saldo = self._saldo

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
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques


    def __str__(self):
        return f"""\
Agência:\t{self.agencia}
C/C:\t\t{self.numero}
Titular:\t{self.cliente._nome}
"""

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionarTransacao(self, transacao):
        self._transacoes.append(transacao)


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
        self._endereco = endereco
        self._contas = []

    @property
    def endreco(self):
        return self._endereco
    
    @property
    def contas(self):
        return self._contas
    
    def realizarTransacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionarConta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, dataNascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._dataNascimento = dataNascimento


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

def addUsuario(userName, cpf, dataNascimento, endereco):
    novoUsuario = PessoaFisica(cpf=cpf, endereco=endereco, nome=userName, dataNascimento=dataNascimento)
    usuarios.append(novoUsuario)
    print("Usuário cadastrado com sucesso")

def addConta(usuario, numero):
    conta = ContaCorrente.novaConta(cliente=usuario, numero=numero)
    print(conta)
    contas.append(conta)
    

def listarContas(cpf):
    print("----------------------------------------------------------")
    for c in contas:
        if c.cliente._cpf == cpf:
            print(c)
    print("----------------------------------------------------------")

def buscarUsuarios(cpf, usuarios):
    for u in usuarios:
        if u._cpf == cpf:
            return u

def opcao(opt):
    global usuarios
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
        cpf = input("Digite um cpf: ")
        res = buscarUsuarios(cpf, usuarios)
        if res == None:
            userName = input("Nome: ")
            dataNascimento = input("Data de nascimento (yyyy-MM-dd): ")
            endereco = input("Endereço: ")
            addUsuario(userName, cpf, dataNascimento, endereco)
        else:
            print("CPF já cadastrado")
        return True
    elif opt == "c":
        cpf = input("Digite um cpf: ")
        usuario = buscarUsuarios(cpf, usuarios)
        if usuario != None:
            numero = len(contas) + 1
            addConta(usuario=usuario, numero=numero)
        else:
            print("Usuário não encontrado")
        return True 
    elif opt == "l":
        cpf = input("Digite um cpf: ")
        usuario = buscarUsuarios(cpf=cpf, usuarios=usuarios)
        if usuario == None:
            print("Usuário não encontrado")
        else:    
            listarContas(cpf)
        
        return True
    elif opt == "q":
        return False
    else:
        return True

main()
