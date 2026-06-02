def alguem_e_dobro_ordenada(lista):
    esquerda = 0
    direita = 0
    n = len(lista)

    while esquerda < n and direita < n:
        if esquerda != direita and lista[direita] == 2 * lista[esquerda]:
            return f"Sim, os números {lista[esquerda]} e {lista[direita]}"
        elif lista[direita] < 2 * lista[esquerda]:
            direita += 1
        else:
            esquerda += 1
    return "Não"


V = [3, 6, 9, 14, 19, 21, 25, 33, 42, 45]
print(alguem_e_dobro_ordenada(V))