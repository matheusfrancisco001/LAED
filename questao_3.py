def mediana_duas_listas(U, V):
    n = len(U)
    inicio = 0
    fim = n

    while inicio <= fim:
        particao_U = (inicio + fim) // 2
        particao_V = n - particao_U

        max_esq_U = float('-inf') if particao_U == 0 else U[particao_U - 1]
        min_dir_U = float('inf') if particao_U == n else U[particao_U]

        max_esq_V = float('-inf') if particao_V == 0 else V[particao_V - 1]
        min_dir_V = float('inf') if particao_V == n else V[particao_V]

        if max_esq_U <= min_dir_V and max_esq_V <= min_dir_U:
            return (max(max_esq_U, max_esq_V) + min(min_dir_U, min_dir_V)) / 2.0
        elif max_esq_U > min_dir_V:
            fim = particao_U - 1
        else:
            inicio = particao_U + 1

U = [1, 3, 6, 7, 10]
V = [11, 15, 17, 19, 21]
print(mediana_duas_listas(U, V))