#acumulador
acumulador = 0


num = int(input('digite um numero: '))
while num > 0:
    acumulador += num
    num = int(input('digite um numero: '))
print(f'a soma dos numero é: {acumulador}')