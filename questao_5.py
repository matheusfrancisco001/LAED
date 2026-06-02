def k_repeticoes(lista, k):
    contagem = {}
    for num in lista:
        contagem[num] = contagem.get(num, 0) + 1
        if contagem[num] >= k:
            return f"Sim, o {num}"
    return "Não"

V = [7, 1, 9, 1, 7, 3, 9, 2, 1, 6, 8, 3]
k = 3
print(k_repeticoes(V, k))