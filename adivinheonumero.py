#importando bibliotecas necessárias
import random
from time import sleep


print('Olá! Você terá que adivinhar o número que eu pensei! Escolha um número de 0 a 10.')
numcomp = random.randint(0,10)

#loop to start the game
while True:
    numjog = int(input('Escolha um número de 0 a 10: '))
    #loop to choose only between 0 and 10
    while numjog < 0 or numjog > 10:
        numjog = int(input('Por favor, digite apenas entre 0 e 10: '))
    #conditional for answer is correct or not
    if numjog == numcomp:
        print(f'Parabéns, você acertou o número! Eu escolhi o número {numcomp}!')
        
    else:
        print(f'Infelizmente você errou o número! Eu escolhi o número {numcomp} e você escolheu {numjog}.')
    #asks the user if they to continue or not
    escolha = str(input('Você quer jogar de novo? [Sim/Não]: ')).strip().upper()
    while escolha not in 'SIMNÃO':
        escolha = str(input('Por favor, responda apenas com SIM ou NÃO: ')).strip().upper()
    if escolha == 'SIM':
        numcomp = random.randint(0,10)
    else: 
        break
