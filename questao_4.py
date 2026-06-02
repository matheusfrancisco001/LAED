def impar_impar(lista):
    contagem = {}
    for num in lista:
        contagem[num] = contagem.get(num, 0) + 1

    for num, qtd in contagem.items():
        if num % 2 != 0 and qtd % 2 != 0:
            return f"Sim, o {num}"
    return "Não"


V = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]
print(impar_impar(V))