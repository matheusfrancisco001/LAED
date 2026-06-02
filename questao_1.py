def terceiro_maior(lista):
    lista_unica = list(set(lista))
    lista_unica.sort(reverse=True)
    if len(lista_unica) >= 3:
        return lista_unica[2]
    return None

V = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]
print(terceiro_maior(V))