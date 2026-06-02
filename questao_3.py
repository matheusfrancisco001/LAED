def busca_aproximada(lista, k):
    if not lista:
        return None

    mais_proximo = lista[0]
    menor_diferenca = abs(lista[0] - k)

    for numero in lista:
        if numero == k:
            return f"O número {k} está na lista!"

        diferenca_atual = abs(numero - k)

        if diferenca_atual < menor_diferenca:
            menor_diferenca = diferenca_atual
            mais_proximo = numero

    return f"Não está lá, mas eu encontrei o {mais_proximo}"


V = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]
k = 31
print(busca_aproximada(V, k))