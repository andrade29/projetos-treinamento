#import libraries
from random import randint 
from time import sleep

#main def
def PCadivinhaNUMERO(numjog):
    #pc is thinking about the number
    print('O computador está pensando', end='',flush=True)
    sleep(1)
    print('.',end='',flush=True)
    sleep(1)
    print('.',end='',flush=True)
    sleep(1)
    print('.',end='',flush=True)
    sleep(1)
    numPC = randint(0,10)
    #the parameter must be between 0 and 10
    while numjog < 0 or numjog > 10:
        numjog = int(input('\nEI! Por favor, apenas número entre 0 e 10: '))
        print('O computador está pensando', end='',flush=True)
        sleep(1)
        print('.',end='',flush=True)
        sleep(1)
        print('.',end='',flush=True)
        sleep(1)
        print('.',end='',flush=True)
        sleep(1)
    #the pc asking for user if he got it right the number
    escolha = str(input(f'\nEu pensei no número {numPC}, consegui acertar? [SIM/NÃO]: ')).upper().strip()
    
    #situations that can occur
    while escolha not in 'SIMNÃO': 
        escolha = str(input(f'Não entendi!!Pode repetir?\nEu pensei no número {numPC}, consegui acertar? [SIM/NÃO]: ')).upper().strip()
    
    if escolha == 'SIM' and numPC == numjog:
        print(f'AHA, consegui acertar! O número foi {numjog}.')
    
    elif escolha == 'SIM' and numPC != numjog:
        print(f'OW, acho que você está querendo me enganar! Eu errei o número! o seu número foi {numjog} e o meu {numPC}.')
    
    elif escolha == 'NÃO' and numPC != numjog:
        print(f'Ah que pena! Eu acabei errando, talvez na próxima! O seu número é {numjog} e o meu {numPC}.')
    
    elif escolha == 'NÃO' and numPC == numjog:
        print(f'EI! Acho que está se confundindo! Eu acertei! Eu escolhi o {numPC} e você o {numjog}.')   

    print('\nFoi um bom jogo! Até a próxima!!') 

#value of parameter  
numescolhido = int(input('Digite um número entre 0 e 10 para o computador adivinhar!: '))
PCadivinhaNUMERO(numescolhido)