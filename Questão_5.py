class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# a) Algoritmo
def intercalar(p1, p2):
    dummy = Node(0)
    cauda = dummy

    while p1 and p2:
        if p1.val <= p2.val:
            cauda.next = p1
            p1 = p1.next
        else:
            cauda.next = p2
            p2 = p2.next
        cauda = cauda.next

    if p1:
        cauda.next = p1
    else:
        cauda.next = p2

    return dummy.next

# b) Analise de tempo
# Percorre os nos das duas listas ordenadas comparando os valores.
# O tempo e O(n + m), sendo n o tamanho de p1 e m o tamanho de p2.