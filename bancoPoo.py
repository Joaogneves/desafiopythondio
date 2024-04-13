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

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        if valor > self._limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_saques >= self._limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        else:
            return super().sacar(valor)

        return False


    def __str__(self):
        return f"""
Agência: {self.agencia}
C/C: {self.numero}
Titular: {self.cliente._nome}
"""

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionarTransacao(self, transacao):
        self._transacoes.append({
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
            })


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucessoTransacao = conta.sacar(self.valor)

        if sucessoTransacao:
            conta.historico.adicionarTransacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucessoTransacao = conta.depositar(self.valor)

        if sucessoTransacao:
            conta.historico.adicionarTransacao(self)

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


def addUsuario(userName, cpf, dataNascimento, endereco):
    novoUsuario = PessoaFisica(cpf=cpf, endereco=endereco, nome=userName, dataNascimento=dataNascimento)
    usuarios.append(novoUsuario)
    print("Usuário cadastrado com sucesso")

def addConta(usuario, numero):
    conta = ContaCorrente.novaConta(cliente=usuario, numero=numero)
    contas.append(conta)
    usuario.contas.append(conta)
    print("Conta criada com sucesso!")
    

def listarContas(cpf):
    contasCliente = []
    cliente = buscarUsuarios(cpf=cpf, usuarios=usuarios)
    print("----------------------------------------------------------")
    for c in contas:
        if c.cliente._cpf == cpf:
            contasCliente.append(c)
    if contasCliente == []:
        print("Não encontrado contas para esse cliente:")
        res = input("Deseja adicionar uma nova conta? (s/n)")
        if res == "s":
            numero = len(contas) + 1
            addConta(usuario=cliente, numero=numero)
    else:
        for co in contasCliente:
            print(co)
    print("----------------------------------------------------------")

def buscarUsuarios(cpf, usuarios):
    for u in usuarios:
        if u._cpf == cpf:
            return u

def encontrarConta(cpf):
    for c in contas:
        if c.cliente._cpf == cpf:
            return c    

def depositar(cpf):
    usuario = buscarUsuarios(cpf=cpf, usuarios=usuarios)
    if not usuario:
        print("Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do depósito: R$"))
    transacao = Deposito(valor)

    conta = encontrarConta(cpf=cpf)
    if not conta:
        return
    
    usuario.realizarTransacao(conta, transacao)

def sacar(cpf):
    usuario = buscarUsuarios(cpf=cpf, usuarios=usuarios)
    if not usuario:
        print("Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do saque: R$"))
    transacao = Saque(valor)

    conta = encontrarConta(cpf=cpf)
    if not conta:
        return
    
    usuario.realizarTransacao(conta, transacao)

def exibirExtrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = buscarUsuarios(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    conta = encontrarConta(cpf)
    if not conta:
        return

    print("---------------- EXTRATO ----------------")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"{transacao['tipo']}: R$ {transacao['valor']:.2f}\n"
            

    print(extrato)
    print(f"Saldo: R$ {conta.saldo:.2f}")
    print("----------------------------------------")


def opcao(opt):
    global usuarios
    if opt == "d":
        cpf = input("Digite um cpf: ")
        depositar(cpf=cpf)
        return True
    elif opt == "s":
        cpf = input("Digite um cpf: ")
        sacar(cpf=cpf)
        return True
    elif opt == "e":
        exibirExtrato(clientes=usuarios)
        return True
    elif opt == "u":
        cpf = input("Digite um cpf: ")
        res = buscarUsuarios(cpf, usuarios)
        if res == None:
            print("------------- Novo cliente --------------")
            print(f"CPF: {cpf}")
            userName = input("Informe o nome completo: ")
            dataNascimento = input("Informe a data de nascimento (dd-MM-aaaa): ")
            endereco = input("Informe o endereço: ")
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
