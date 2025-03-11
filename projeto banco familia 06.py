saldo = 1000
# banco familia 06
print('SEJA BEM VINDO AO BANCO FAMILIA 06')

while True:
    print('1 - Depósito')
    print('2 - Saldo')
    print('3 - Saque')
    print('4 - Emprestimo')
    print('5 - Suporte')
    print('6 - Sair')

    opção = int(input('ESCOLHA A OPÇÃO DESEJADA:'))
    
    if opção == 1:
        print('Depósito')
        depósito = float(input('valor do depósito:'))
        saldo += depósito
        print(f'depósito no valor de R$ {depósito} efetuado com sucesso')
    
    elif opção == 2:
        print(f'seu saldo é de R$ {saldo}')
    
    elif opção == 3:
        print('Saque')
        saque = float(input('valor do saque:'))
        if saque <= saldo:
            saldo -= saque
            print(f'saque no valor R$ {saque} efetuado com sucesso')
        else:
            print('Saldo insuficiente')

    elif opção == 4:
        print('Emprestimo')
        print('não ha proposta de emprestimo disponivel no momento')
    
    elif opção == 5:
        print('Suporte')
        print('Para suporte, ligue para 0800-123-456')
    
    elif opção == 6:
        print('obrigado por utilizar o banco familia 06')
        break
    
    else:
        print('Opção inválida, por favor tente novamente')
    
    realizar_outra = input('gostaria de realizar outra operação? (sim/não): ').strip().lower()
    if realizar_outra != 'sim':
        print('OBRIGADO POR UTILIZAR O BANCO FAMILIA 06')
        break