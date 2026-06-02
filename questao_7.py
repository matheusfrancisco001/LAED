def repetidos_proximos(lista, k):
    posicoes = {}
    for i, num in enumerate(lista):
        if num in posicoes and (i - posicoes[num]) <= k:
            return f"Sim, o {num}"
        posicoes[num] = i
    return "Não"

V = [2, 1, 9, 7, 6, 3, 9, 4, 2, 6, 1, 3]
k = 4
print(repetidos_proximos(V, k))