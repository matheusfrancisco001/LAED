class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# a) Algoritmo
def mais_frequente(p):
    if not p:
        return None

    cont = {}
    atual = p
    while atual:
        if atual.val in cont:
            cont[atual.val] += 1
        else:
            cont[atual.val] = 1
        atual = atual.next

    melhor_val = None
    max_vezes = 0
    for chave in cont:
        if cont[chave] > max_vezes:
            max_vezes = cont[chave]
            melhor_val = chave

    return melhor_val, max_vezes

# b) Analise de tempo
# Faz uma passada para contar a frequencia e outra pelas chaves do dicionario.
# O tempo e O(n).