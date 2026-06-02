def segundo_maior_impar(lista):
    impares = []
    for num in lista:
        if num % 2 != 0:
            impares.append(num)

    impares_unicos = list(set(impares))
    impares_unicos.sort(reverse=True)

    if len(impares_unicos) >= 2:
        return impares_unicos[1]
    return None


V = [9, 42, 21, 14, 28, 3, 19, 32, 46, 6]
print(segundo_maior_impar(V))