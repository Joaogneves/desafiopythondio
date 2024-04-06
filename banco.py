menu = """
    [d] Deposito
    [s] Sacar
    [e] Extrato
    [q] Sair
"""

saldo = 0.0
limite = 500.0
extrato = []
saques = 0

while True:
    opt = input(menu)

    if opt == "d":
        valor_deposito = float(input("Qual valor a ser depositado: R$"))
        if valor_deposito <= 0:
            print("Valor do deposito precisa ser maior que zero!")
        else: 
            saldo += valor_deposito
            extrato_template = f"Deposito: R${valor_deposito:.2f}"
            extrato.append(extrato_template)
    elif opt == "s":
        if saques >= 3:
            print("Número de saques diários excedido")
        else:
            valor_saque = float(input("Valor do saque à ser feito: R$")) 
            if valor_saque < 500 and valor_saque < saldo:
                saldo -= valor_saque
                extrato_template = f"Saque: R${valor_saque:.2f}"
                extrato.append(extrato_template)
                saques += 1
            else:
                if valor_saque > saldo:
                    print("Saque não concluido por falta de saldo")
                else:
                    print("Saque não concluido! Limite de saque R$500,00")

    elif opt == "e":
        print("------------------------------")
        print("___________Extrato____________")
        if len(extrato) == 0:
            print("Não foram realizadas movimentações")
        else:
            for i in range(len(extrato)):
                print(extrato[i])
        print(f"Saldo: R${saldo:.2f}")
        print("------------------------------")
    elif opt == "q":
        break
    else:
        print("Escolha uma opção valida")
        