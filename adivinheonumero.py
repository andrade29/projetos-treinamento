import random
from time import sleep


print('Olá! Você terá que adivinhar o número que eu pensei! Escolha um número de 0 a 10.')
numcomp = random.randint(0,10)

while True:
    numjog = int(input('Escolha um número de 0 a 10: '))
    while numjog < 0 or numjog > 10:
        numjog = int(input('Por favor, digite apenas entre 0 e 10: '))
    if numjog == numcomp:
        print(f'Parabéns, você acertou o número! Eu escolhi o número {numcomp}!')
        
    else:
        print(f'Infelizmente você errou o número! Eu escolhi o número {numcomp} e você escolheu {numjog}.')
    
    escolha = str(input('Você quer jogar de novo? [Sim/Não]: ')).strip().upper()
    while escolha not in 'SIMNÃO':
        escolha = str(input('Por favor, responda apenas com SIM ou NÃO: ')).strip().upper()
    if escolha == 'SIM':
        numcomp = random.randint(0,10)
    else: 
        break

    




