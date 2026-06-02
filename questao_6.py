def elementos_mais_proximos(lista):
    if len(lista) < 2:
        return None

    lista_ordenada = sorted(lista)
    menor_dif = abs(lista_ordenada[1] - lista_ordenada[0])
    par = (lista_ordenada[0], lista_ordenada[1])

    for i in range(1, len(lista_ordenada) - 1):
        dif = abs(lista_ordenada[i + 1] - lista_ordenada[i])
        if dif < menor_dif:
            menor_dif = dif
            par = (lista_ordenada[i], lista_ordenada[i + 1])

    return f"os elementos {par[0]} e {par[1]}"


V = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]
print(elementos_mais_proximos(V))