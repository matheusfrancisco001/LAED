def elemento_isolado(lista):
    conjunto = set(lista)
    isolados = []
    for num in lista:
        if (num - 1) not in conjunto and (num + 1) not in conjunto:
            isolados.append(num)

    if isolados:
        return f"Sim, o {isolados[0]}"
    return "Não"


V = [17, 2, 8, 1, 7, 13, 9, 12, 4, 16]
print(elemento_isolado(V))