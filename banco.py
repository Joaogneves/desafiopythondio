saldo = 0
extrato = []
saques = 0
usuario = {}
usuarios = []
conta = {}
contas = []

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

def cadastrarUsuario(userName, cpf, dataNascimento, endereco):
    global usuario
    global usuarios
    novoUsuario = {'nome': userName, 'cpf': cpf, 'dataNascimento': dataNascimento, "endereco": endereco}
    usuarios.append(novoUsuario)
    print("Usuário cadastrado com sucesso")
 

def getUser(cpf): 
    global usuarios
    for u in usuarios:
        if u['cpf'] == cpf:
            return u
        

    return None
        
def cadastrarConta(cpf):
    AGENCIA = "0001"
    global conta
    global contas
    res = getUser(cpf)
    if res == None:
        print("Usuário não cadastrado!")
        return
    print(res)
    nConta = len(contas) + 1
    conta = {"agencia": AGENCIA, "c/c": nConta, "usuario": res}    
    contas.append(conta)
    print("Conta criada com sucesso")

def listarContas():
    print("----------------------------------------------------------")
    for c in contas:
        listaContas = f"""
        Agência: {c['agencia']},
        c/c:     {c['c/c']},
        Titular: {c['usuario']['nome']}
        """
        print(listaContas)
        print("----------------------------------------------------------")

def main():
    while True:
        print(exibirMenu())
        opt = input(">>> ")
        if opt == "d":
            valor_deposito = float(input("Qual valor a ser depositado: R$"))
            deposito(valor_deposito)
        elif opt == "s":
            valor_saque = float(input("Valor do saque à ser feito: R$"))
            saque(valor_saque)
        elif opt == "e":
            gerarExtrato()
        elif opt == "u":
            cpf = input("Insira o cpf: ")
            res = getUser(cpf)
            if res == None:
                userName = input("Nome: ")
                dataNascimento = input("Data de nascimento (yyyy-MM-dd): ")
                endereco = input("Endereço: ")
                cadastrarUsuario(userName, cpf, dataNascimento, endereco)
            else: 
                print("CPF já cadastrado!")
        elif opt == "c":
            cpf = input("Insira o cpf: ")
            cadastrarConta(cpf)
        elif opt == "l":
            listarContas()
        elif opt == "q":
            break
        else:
            print("Escolha uma opção valida")


main()
        