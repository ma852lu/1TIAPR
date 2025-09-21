'''
preco = float(input('digite o valor do produto: '))
if preco > 100:
    desconto = preco * 0.10
    preco_final = preco - desconto
    print(f'preço final com desconto: R${preco_final:.2f}')
else:
    print(f'preço final sem desconto: R${preço:.2f}')
'''

p = float(input('digite o valor do produto: '))
print(f'preço final: R$ {p*0.9:.2f}' if p > 100 else f'preço final: R$ {p:.2f}')

