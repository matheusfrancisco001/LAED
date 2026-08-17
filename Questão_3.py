class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# a) Algoritmo
def inverter_lista(p):
    ant = None
    atual = p
    while atual:
        prox = atual.next
        atual.next = ant
        ant = atual
        atual = prox
    return ant

# b) Analise de tempo
# Percorre a lista invertendo os ponteiros um por um.
# O tempo e O(n).