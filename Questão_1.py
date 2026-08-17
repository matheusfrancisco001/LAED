class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# a) Algoritmo
def elemento_central(p):
    if not p:
        return None

    lento = p
    rapido = p

    while rapido.next and rapido.next.next:
        lento = lento.next
        rapido = rapido.next.next

    return lento.val

# b) Analise de tempo
# Usa dois ponteiros onde o rapido anda o dobro do lento.
# Percorre a lista em uma passada unica, entao o tempo e O(n).