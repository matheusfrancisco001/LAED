class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# a) Algoritmo
def trocar_com_proximo(p, no):
    prox = no.next
    if not prox:
        return p

    ant = no.prev
    depois = prox.next

    if ant:
        ant.next = prox
    else:
        p = prox

    prox.prev = ant
    prox.next = no

    no.prev = prox
    no.next = depois

    if depois:
        depois.prev = no

    return p

def varredura(p):
    if not p:
        return p

    q = p
    while q.next:
        if q.val > q.next.val:
            p = trocar_com_proximo(p, q)
        else:
            q = q.next
    return p

# b) Analise de tempo
# Uma varredura completa passa por todos os pares adjacentes trocando os nos.
# O tempo de uma varredura e O(n).