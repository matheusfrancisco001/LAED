class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# a) Algoritmo
def atualizar(p, x, y):
    if not p:
        return p

    # Busca o no com valor x
    atual = p
    while atual and atual.val != x:
        atual = atual.next

    if not atual:
        return p

    atual.val = y

    # Remove o no da posicao atual
    if atual.prev:
        atual.prev.next = atual.next
    else:
        p = atual.next

    if atual.next:
        atual.next.prev = atual.prev

    atual.prev = None
    atual.next = None

    # Reinsere na posicao correta mantendo ordenado
    if not p:
        return atual

    if atual.val <= p.val:
        atual.next = p
        p.prev = atual
        return atual

    pos = p
    while pos.next and pos.next.val < atual.val:
        pos = pos.next

    atual.next = pos.next
    atual.prev = pos
    if pos.next:
        pos.next.prev = atual
    pos.next = atual

    return p

# b) Analise de tempo
# Faz a busca, remocao em O(1) dos ponteiros e reinsercao ordenada percorrendo a lista.
# O tempo total no pior caso e O(n).