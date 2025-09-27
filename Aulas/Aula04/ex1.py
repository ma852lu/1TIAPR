matriz = [
    [1, 2, 3],  # linha 0
    [4, 5, 6],  # linha 1
    [7, 8, 9]   # linha 2
]

T = [list(row) for row in zip(*matriz)]  # desempacota A em zip, cada tupla é uma coluna; list(...) converte tupla em lista

print("A:")
for r in matriz:
    print(r)  # imprime cada linha de A

print("Transposta T:")
for r in T:
    print(r)  # imprime cada linha de T




matrix = [
    [1, 2, 3],  # linha 0
    [4, 5, 6],  # linha 1
    [7, 8, 9]   # linha 2
]

# zip(*matrix) gera tuplas que representam colunas da matrix
# column_tuple é cada uma dessas tuplas; list(column_tuple) converte para lista
transposed_matrix = [list(column_tuple) for column_tuple in zip(*matrix)]

print("Matriz original (matrix):")
for linha in matrix:
    print(linha)

print("\nMatriz transposta (transposed_matrix):")
for linha in transposed_matrix:
    print(linha)