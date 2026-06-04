def tem_linhas_iguais(M):
    linhas_vistas = {}
    for i, linha in enumerate(M):
        tupla_linha = tuple(linha)
        if tupla_linha in linhas_vistas:
            return f"Sim, as linhas {linhas_vistas[tupla_linha] + 1} e {i + 1} são exatamente iguais"
        linhas_vistas[tupla_linha] = i
    return "Não"

M = [
    [3, 9, 4, 2, 4, 1, 8, 5, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [5, 8, 2, 3, 9, 8, 4, 1, 7],
    [8, 3, 4, 2, 3, 1, 3, 9, 4],
    [3, 7, 2, 9, 4, 2, 1, 2, 3],
    [7, 5, 3, 1, 2, 4, 5, 8, 2],
    [4, 7, 3, 6, 5, 1, 9, 3, 2],
    [1, 5, 3, 2, 9, 8, 7, 6, 5],
    [3, 9, 4, 2, 4, 1, 8, 5, 1]
]
print(tem_linhas_iguais(M))