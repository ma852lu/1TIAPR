#while    
lista_num = [1, 2, 3, 4, 5]

soma = sum(lista_num)

print(soma)

resultado = 0
for num in lista_num:
    resultado += num

print(resultado)

while True:
    comando = input('Digite "sair" paa encerrar:')
    if comando == 'sair':
        break
    print('voce digitou:', comando)
    
    
    
    
#while simplificado
contador = 0
while contador < 8:
    print('contador', contador)
    contador += 1


