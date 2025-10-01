matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[1][2])

#adicioando uma nova linha a matriz

nova_linha = [10, 11, 12]
matriz.append(nova_linha)

'''
#imprimindo a matriz atualizada
for linha in matriz:
    print(linha)
'''

#adicionando um elemento
matriz[1].insert(0, 100)


#usando 'del' para rmover a segunda linha
del matriz[1]


#imprimindo a matriz apos a remoção da segunda linha
print('matriz apos a remoção da segunda linha:')
for linha in matriz:
    print(linha)


#Itera sobre cada linha da matriz
for linha in matriz:
    #iterar sobre cada elemento da linha
    for elemento in linha:
        print(elemento, end=' ')
    
    #imprimir uma nova linha após cada linha da matriz
    print() 




