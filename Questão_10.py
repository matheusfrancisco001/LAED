class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# a) Operacoes
def busca(L, x):
    if not L:
        return False

    sublista_idx = -1
    for i in range(len(L)):
        if L[i].val <= x:
            sublista_idx = i
        else:
            break

    if sublista_idx == -1:
        return False

    atual = L[sublista_idx]
    while atual:
        if atual.val == x:
            return True
        if atual.val > x:
            return False
        atual = atual.next

    return False

def insercao(L, x):
    if not L:
        L.append(Node(x))
        return L

    idx = 0
    for i in range(len(L)):
        if L[i].val <= x:
            idx = i
        else:
            break

    novo = Node(x)
    sub = L[idx]

    if x < sub.val:
        novo.next = sub
        sub.prev = novo
        L[idx] = novo
        return L

    atual = sub
    while atual.next and atual.next.val < x:
        atual = atual.next

    novo.next = atual.next
    novo.prev = atual
    if atual.next:
        atual.next.prev = novo
    atual.next = novo

    return L

def remocao(L, x):
    if not L:
        return L

    for i in range(len(L)):
        atual = L[i]
        while atual:
            if atual.val == x:
                if atual.prev:
                    atual.prev.next = atual.next
                else:
                    L[i] = atual.next

                if atual.next:
                    atual.next.prev = atual.prev

                if L[i] is None:
                    L.pop(i)
                return L
            atual = atual.next

    return L

# b) Analise de tempo
# A busca e insercao encontram a sublista no vetor em O(k) e percorrem a sublista em O(n/k).
# O tempo e O(k + n/k).