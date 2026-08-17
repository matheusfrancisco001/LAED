class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# a) Algoritmo
def particionar(p, k):
    d_menor = Node(0)
    d_maior = Node(0)
    t_menor = d_menor
    t_maior = d_maior

    atual = p
    while atual:
        prox = atual.next
        atual.next = None
        if atual.val <= k:
            t_menor.next = atual
            t_menor = atual
        else:
            t_maior.next = atual
            t_maior = atual
        atual = prox

    t_menor.next = d_maior.next
    return d_menor.next

# b) Analise de tempo
# Varre a lista separando quem e <= k e quem e > k e junta as duas partes no final.
# O tempo e O(n).