print('-='*30)
def operacoes():
    while True:
        escolha = str(input('Escolha a operação que deseja realizar:\n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n->')).strip().upper()
        if escolha == 'ADIÇÃO':
            num = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            adicao = num + num2 
            print(f'O resultado da soma dos dois números é {adicao:.2f}')
        elif escolha == 'SUBTRAÇÃO':
            num = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            sub = num - num2 
            print(f'O resultado da subtração é {sub:.2f}')
        elif escolha == 'MULTIPLICAÇÃO':
            num = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            mult = num*num2 
            print(f'O resultado da multiplicação é {mult:.2f}')
        elif escolha == 'DIVISÃO':
            num = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            div = num/num2
            print(f'O resultado da divisão é {div:.2f}')
        opcao = str(input('Quer fazer outra operação?[SIM/NÃO]: ')).strip().upper()
        while opcao not in 'SIMNÃO':
            opcao = str(input('Quer fazer outra operação?[SIM/NÃO]: ')).strip().upper()
        if opcao == 'SIM':
            return operacoes()
        else:
            print('Encerrado...')   
            print('-='*30)
            break
operacoes()
