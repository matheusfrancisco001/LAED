def maior_impar(lista):
    maior = None
    for numero in lista:
        if numero % 2 != 0:
            if maior is None or numero > maior:
                 maior = numero
    return maior

V = [9,42,21,14,28,3,19,32,46,6]
print(maior_impar(V))
    