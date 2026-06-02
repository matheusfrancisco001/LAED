def sao_permutacoes(U, V):
    if len(U) != len(V):
        return False

    contagem_U = {}
    contagem_V = {}

    for num in U:
        contagem_U[num] = contagem_U.get(num, 0) + 1
    for num in V:
        contagem_V[num] = contagem_V.get(num, 0) + 1

    return contagem_U == contagem_V


U = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
V = [7, 2, 3, 1, 6, 5, 9, 10, 4, 8]
print(sao_permutacoes(U, V))