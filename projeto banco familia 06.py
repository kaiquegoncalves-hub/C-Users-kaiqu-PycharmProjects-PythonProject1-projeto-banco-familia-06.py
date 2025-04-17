# Sistema de cadastro de clientes e operações bancárias

clientes = []
contas = {}

limite_diario_saque = 500
limite_saque = 3

def cadastrar_cliente():
    print("\n--- Cadastro de Cliente ---")
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    cpf = input("CPF (somente números): ")
    endereco = {
        "rua": input("Nome da rua: "),
        "numero": input("Número da casa: "),
        "bairro": input("Bairro: "),
        "cidade": input("Cidade: "),
        "estado": input("Estado: "),
        "sigla": input("Sigla do estado (ex: SP): ")
    }

    # Verificar se o CPF já está cadastrado
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print("Erro: CPF já cadastrado.")
            return

    # Criar cliente
    cliente = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    clientes.append(cliente)

    # Criar conta vinculada ao cliente
    agencia = input("Número da agência: ")

    # Verificar se o CPF já possui uma conta
    if cpf in contas:
        print("Erro: Este CPF já possui uma conta cadastrada.")
        return

    contas[cpf] = {
        "agencia": agencia,
        "saldo": 0,
        "extrato": "",
        "limite_saque": limite_saque
    }

    print("Cliente e conta cadastrados com sucesso!")

def acessar_conta():
    print("\n--- Acessar Conta ---")
    cpf = input("Digite o CPF (somente números): ")

    # Verificar se a conta existe para o CPF
    if cpf not in contas:
        print("Erro: Conta não encontrada para este CPF.")
        return None

    return contas[cpf]

def menu_bancario(conta):
    while True:
        print("\n1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Sair")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            valor_deposito = float(input("Digite o valor do depósito: "))
            if valor_deposito > 0:
                conta["saldo"] += valor_deposito
                conta["extrato"] += f"Depósito: R$ {valor_deposito:.2f}\n"
                print("Depósito efetuado com sucesso.")
            else:
                print("Depósito inválido.")

        elif opcao == 2:
            if conta["limite_saque"] > 0:
                valor_saque = float(input("Digite o valor que deseja sacar: "))
                if valor_saque > 0 and valor_saque <= conta["saldo"] and valor_saque <= limite_diario_saque:
                    conta["saldo"] -= valor_saque
                    conta["limite_saque"] -= 1
                    conta["extrato"] += f"Saque: R$ {valor_saque:.2f}\n"
                    print("Saque realizado com sucesso.")
                elif valor_saque > conta["saldo"]:
                    print("Saldo insuficiente.")
                elif valor_saque > limite_diario_saque:
                    print("Limite diário de saque excedido.")
                else:
                    print("Valor de saque inválido.")
            else:
                print("Limite de saques diários excedido.")

        elif opcao == 3:
            print("Extrato:")
            print(conta["extrato"])
            print(f"Saldo atual: R$ {conta['saldo']:.2f}")

        elif opcao == 4:
            print("Saindo do sistema bancário...")
            break

        else:
            print("Opção inválida.")

while True:
    print("\n--- Sistema Bancário ---")
    print("1. Cadastrar Cliente")
    print("2. Acessar Conta")
    print("3. Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        cadastrar_cliente()
    elif opcao == 2:
        conta = acessar_conta()
        if conta:
            menu_bancario(conta)
    elif opcao == 3:
        print("Obrigado por utilizar o sistema bancário!")
        break
    else:
        print("Opção inválida.")
