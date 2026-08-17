class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# a) Algoritmo
def intersecao(p1, p2):
    elementos_p2 = set()
    atual = p2
    while atual:
        elementos_p2.add(atual.val)
        atual = atual.next

    dummy = Node(0)
    cauda = dummy
    adicionados = set()

    atual = p1
    while atual:
        if atual.val in elementos_p2 and atual.val not in adicionados:
            cauda.next = Node(atual.val)
            cauda = cauda.next
            adicionados.add(atual.val)
        atual = atual.next

    return dummy.next

# b) Analise de tempo
# Monta o set com os elementos de p2 em O(m) e varre p1 montando a nova lista em O(n).
# O tempo total e O(n + m).