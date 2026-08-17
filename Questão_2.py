class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# a) Algoritmo
def separar_pares_impares(p):
    d_impar = Node(0)
    d_par = Node(0)
    t_impar = d_impar
    t_par = d_par

    atual = p
    while atual:
        prox = atual.next
        atual.next = None
        if atual.val % 2 != 0:
            t_impar.next = atual
            t_impar = atual
        else:
            t_par.next = atual
            t_par = atual
        atual = prox

    return d_impar.next, d_par.next

# b) Analise de tempo
# Faz uma passada simples dividindo os nos entre duas listas.
# O tempo e O(n).