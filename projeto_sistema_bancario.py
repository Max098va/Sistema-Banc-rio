saldo = 2000
LIMITES_SAQUE = 3
limite = 500
numero_saques = 0
extrato = ''
menu = ('=============MENU===========\n[1] Sacar\n[2] Deposito\n[3] Extrato\n[4] Sair\n')


while True:
    
    opcao = input(menu)

    if opcao == '1':
       
       valor = float(input('Qual o valor do saque: '))
       excedeu_saldo = valor > saldo
       excedeu_saques = numero_saques >= LIMITES_SAQUE
       excedeu_valor_saque = valor > limite
       
       if excedeu_saldo:
           print('Saldo insuficiente')
       elif excedeu_saques:
           print('Operação falhou, Limite para saques excedido')
       elif excedeu_valor_saque:
           print('Operação falhou, valor de limite para saques excedido')
       elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            print('Sacando...\n Retire seu dinheiro na boca do caixa.\n Obrigado por ser nosso cliente :)')
            numero_saques += 1

    elif opcao == '2':
        valor = float(input('Digite o valor do deposito: '))

        if valor >= 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
            print('Deposito efetuado com sucesso!')

        else:
            print('Operação falhou valor invalido!')   
        
    elif opcao == '3':
        print('===========EXTRATO===========')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print('============================')
       
    elif opcao == '4':
        print('Saindo...\n Obrigado por ser nosso cliente até mais :)')
        break
    else:
        print('Operação invalida, por favor selecione novamente a opção desejada')
