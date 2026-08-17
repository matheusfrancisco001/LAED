class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# a) Algoritmo
def duplicar_impares(p):
    atual = p
    while atual:
        if atual.val % 2 != 0:
            novo = Node(atual.val, atual.next)
            atual.next = novo
            atual = novo.next
        else:
            atual = atual.next
    return p

# b) Analise de tempo
# Percorre cada elemento inserindo um novo no logo em seguida quando e impar.
# O tempo e O(n).