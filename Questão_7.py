class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# a) Algoritmo
def remover_copias(p, k):
    dummy = Node(0, p)
    atual = dummy
    while atual.next:
        if atual.next.val == k:
            atual.next = atual.next.next
        else:
            atual = atual.next
    return dummy.next

# b) Analise de tempo
# Percorre a lista checando o proximo no para pular quando o valor for igual a k.
# O tempo e O(n).