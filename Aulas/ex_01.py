'''
lista_mercado = []
lista_mercado.append('banana')
lista_mercado.append('uva')
lista_mercado.append('laranja')
lista_mercado.append('pepino')
lista_mercado.insert(1, 'uva')
lista_mercado.append('banana')
lista_mercado.remove('banana')

lista_mercado.pop(1)

#lista_mercado.clear()

print(lista_mercado.index('laranja'))
print(lista_mercado.count('banana'))

lista_mercado.sort()
lista_mercado.reverse()


lista_mercado.apend(input('Digite um item: '))
print(lista_mercado[])


print(lista_mercado)
'''


lista_num = []
lista_num.append(1)
lista_num.append(2)
lista_num.append(3)
lista_num.append(4)
lista_num.append(5)


soma = sum(lista_num)


lista_palavras = ['bosta', 'merda', 'programa']

frase = ', '.join(lista_palavras) + '.'

print(frase)