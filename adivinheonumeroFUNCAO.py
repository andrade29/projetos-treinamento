from random import randint
from time import sleep 

#def for random number
def numsorteado(numjog):
    while True:
        #loop for number between 0 and 10
        while numjog < 0 or numjog > 10:
            numjog = int(input('Por favor, escolha apenas entre 0 e 10: '))
        numcomp = randint(0,10)
        #conditional if the answer is correct or wrong
        if numjog == numcomp:
            print(f'Parabéns, você acertou o número! O número escolhido foi {numcomp}')
        else:
            print(f'Infelizmente você errou o número! Você escolheu o {numjog} e o número escolhido foi {numcomp}')
            #loop ansking if the user wants to continue or not
            escolha = str(input('Você quer continuar? [Sim/Não]: ')).strip().upper()
            while escolha not in 'SIMNÃO':
                escolha = str(input('Por favor, digite apenas SIM ou NÃO: ')).strip().upper()
            if escolha == 'SIM':
                numcomp = randint(0,10)
                numjog = int(input('Escolha outro número de 0 a 10: '))
            else: 
                break
        
    
#value of the passed parameter
numescolhido = int(input('Escolha um número de 0 a 10: '))
numsorteado(numescolhido)
