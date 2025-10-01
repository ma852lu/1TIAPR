A = [
    {1,2,3}
    {4,5,6}
    {7,8,9}
]

B = [
    {9,8,7}
    {6,5,4}
    {3,2,1}
]

matriz_soma = [
    [0,0,0]
    [0,0,0]
    [0,0,0]
]

for l in range(len[A]):
    for j in range(len[A[0]]):
        matriz_soma[l][j] = A[l][j] + B[l][j]

print(matriz_soma)




