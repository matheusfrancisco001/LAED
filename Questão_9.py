class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# a) Algoritmo
def criar_lista_de_listas(p, k):
    if not p:
        return []

    # Conta o total de elementos
    total = 0
    atual = p
    while atual:
        total += 1
        atual = atual.next

    tamanho_bloco = total // k
    resto = total % k

    vetor_L = []
    atual = p

    for i in range(k):
        if not atual:
            break

        vetor_L.append(atual)
        tamanho_atual = tamanho_bloco + (1 if i < resto else 0)

        for _ in range(tamanho_atual - 1):
            if atual:
                atual = atual.next

        if atual:
            prox = atual.next
            atual.next = None
            if prox:
                prox.prev = None
            atual = prox

    return vetor_L

# b) Analise de tempo
# Faz uma passada para contar os nos e outra quebrando os ponteiros nos blocos.
# O tempo total e O(n).