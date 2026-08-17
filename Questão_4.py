class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# a) Algoritmo
def particionar(p, k):
    if not p or not p.next:
        return p

    q = p
    r = p
    while r.next:
        r = r.next

    while q != r and q.prev != r:
        while q != r and q.val <= k:
            q = q.next
        while q != r and r.val > k:
            r = r.prev

        if q != r and q.prev != r:
            q.val, r.val = r.val, q.val

    return p

# b) Analise de tempo
# Os dois ponteiros q e r convergem ate se encontrarem no meio.
# Cada elemento e visitado no maximo uma vez, entao o tempo e O(n).