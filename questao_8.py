def numeros_em_ambas(U, V):
    conjunto_U = set(U)
    conjunto_V = set(V)
    intersecao = conjunto_U.intersection(conjunto_V)

    resultado = list(intersecao)
    resultado.sort()

    if resultado:
        return ", ".join(map(str, resultado))
    return "Nenhum número em comum"


U = [9, 2, 77, 2, 2, 1, 7, 7, 9]
V = [2, 15, 19, 12, 33, 9, 17, 41, 54, 8]
print(numeros_em_ambas(U, V))