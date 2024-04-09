menu = """
    [d] Deposito
    [s] Sacar
    [e] Extrato
    [a] Adicionar Usuario
    [c] Nova Conta
    [q] Sair
"""

saldo = 0
extrato = []
saques = 0
usuario = {}
conta = {}

def exibirMenu():
    global menu
    return menu

def deposito(valor_deposito):
    if valor_deposito <= 0:
        print("Valor do deposito precisa ser maior que zero!")
    else:
        global saldo
        saldo += valor_deposito
        extrato_template = f"Deposito: R${valor_deposito:.2f}"
        extrato.append(extrato_template)

def saque(valor_saque):
    global saques
    global saldo
    if saques >= 3:
        print("Número de saques diários excedido")
    else: 
        if valor_saque < 500 and valor_saque <= saldo:
            saldo -= valor_saque
            extrato_template = f"Saque: R${valor_saque:.2f}"
            extrato.append(extrato_template)
            saques += 1
        else:
            if valor_saque > saldo:
                print("Saque não concluido por falta de saldo")
            else:
                print("Saque não concluido! Limite de saque R$500,00")

def gerarExtrato():
    global extrato
    print("------------------------------")
    print("___________Extrato____________")
    if len(extrato) == 0:
        print("Não foram realizadas movimentações")
    else:
        for e in extrato:
            print(e)
    print(f"Saldo: R${saldo:.2f}")
    print("------------------------------")

def cadastrarUsuario():
    global usuario
    novoUsuario = {'nome': userName}
    usuario.update(novoUsuario)
    res = usuario.get('nome')
    print("Nome do usuário inserido:", res)
 

def getUser(cpf): 
    for u in usuario:
        if u     == cpf:
            return True
        return False

def main():
    while True:
        opt = input(exibirMenu())
        if opt == "d":
            valor_deposito = float(input("Qual valor a ser depositado: R$"))
            deposito(valor_deposito)
        elif opt == "s":
            valor_saque = float(input("Valor do saque à ser feito: R$"))
            saque(valor_saque)
        elif opt == "e":
            gerarExtrato()
        elif opt == "a":
            cpf = input("Insira o cpf: ")
            if getUser(cpf):
                userName = input("Nome: ")
                dataNascimento = input("Data de nascimento: ")
                endereco = input("Endereço: ")
                cadastrarUsuario(userName, dataNascimento, endereco)
            else: 
                print("CPF já cadastrado!")
        elif opt == "q":
            break
        else:
            print("Escolha uma opção valida")


main()
        