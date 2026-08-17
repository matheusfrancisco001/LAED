class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# a) Algoritmo
def mover_maior_fim(p):
    if not p or not p.next:
        return p

    maior_val = p.val
    ant_maior = None
    no_maior = p

    ant = p
    atual = p.next
    while atual:
        if atual.val > maior_val:
            maior_val = atual.val
            no_maior = atual
            ant_maior = ant
        ant = atual
        atual = atual.next

    ultimo = ant

    if no_maior == ultimo:
        return p

    if no_maior == p:
        p = p.next
    else:
        ant_maior.next = no_maior.next

    ultimo.next = no_maior
    no_maior.next = None

    return p

# b) Analise de tempo
# Percorre a lista uma única vez para achar o maior e o ultimo nó.
# Logo o tempo e O(n), onde n e a quantidade de elementos.