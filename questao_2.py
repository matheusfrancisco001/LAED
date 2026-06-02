def k_esimo_maior(lista, k):
    lista_unica = list(set(lista))
    lista_unica.sort(reverse=True)
    if len(lista_unica) >= k:
        return lista_unica[k-1]
    return None

V = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]
k = 4
print(k_esimo_maior(V, k))