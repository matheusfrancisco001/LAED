def mais_proximo_media(lista):
    if not lista:
        return None
    media = sum(lista) / len(lista)
    mais_proximo = lista[0]
    menor_diferenca = abs(lista[0] - media)

    for num in lista:
        diferenca = abs(num - media)
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            mais_proximo = num
    return mais_proximo


V = [3, 1, 10, 2, 13, 9, 12, 4, 7]
print(mais_proximo_media(V))