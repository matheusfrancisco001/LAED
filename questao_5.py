def alguem_e_dobro_nao_ordenada(lista):
    conjunto = set(lista)
    for num in lista:
        if (num * 2) in conjunto:
            return f"Sim, os números {num} e {num * 2}"
    return "Não"

V = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]
print(alguem_e_dobro_nao_ordenada(V))