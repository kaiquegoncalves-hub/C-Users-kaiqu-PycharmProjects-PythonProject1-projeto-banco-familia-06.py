# Criar um sistema bancário que simule depósito, saque e extrato.

limite_diario_saque = 500
extrato = ''
limite_saque = 3
saldo = 0

while True:
    print('1. Depósito')
    print('2. Saque')
    print('3. Extrato')
    print('4. Sair')

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        valor_deposito = float(input('Digite o valor do depósito: '))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'Depósito: R$ {valor_deposito:.2f}\n'
            print('Depósito efetuado com sucesso.')
        else:
            print('Depósito inválido.')

    elif opcao == 2:
        if limite_saque > 0:
            valor_saque = float(input('Digite o valor que deseja sacar: '))
            if valor_saque > 0 and valor_saque <= saldo and valor_saque <= limite_diario_saque:
                saldo -= valor_saque
                limite_saque -= 1
                extrato += f'Saque: R$ {valor_saque:.2f}\n'
                print('Saque realizado com sucesso.')
            elif valor_saque > saldo:
                print('Saldo insuficiente.')
            elif valor_saque > limite_diario_saque:
                print('Limite diário de saque excedido.')
            else:
                print('Valor de saque inválido.')
        else:
            print('Limite de saques diários excedido.')

    elif opcao == 3:
        print('Extrato:')
        print(extrato)
        print(f'Saldo atual: R$ {saldo:.2f}')

    elif opcao == 4:
        print('Saindo...')
        break

    else:
        print('Opção inválida.')
