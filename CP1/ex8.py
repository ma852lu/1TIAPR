'''
num = int(input('digite um numero inteiro: '))
if num % 2 == 0:
    print('Par')
elif num % 5 == 0:
    print('este número é multiplo de 5')
else: 
    print('Outro número')
'''

n=int(input('digite um número inteiro: '));print('Par' if n%2==0 else 'Multiplo de 5' if n%5==0 else 'outro numero')  


