#random
import random

tentativas = 3
numero = random.randint(1, 10)

while tentativas > 0:
    palpite = int(input('digite um numero entra 1 a 10: '))
    if palpite  == numero: 
        print('voce acertou')
        break
    else:
        tentativas -= 1 
        print(f'vc errou. tentar de novo')