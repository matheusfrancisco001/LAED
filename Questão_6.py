class NodeEsparso:
    def __init__(self, valor=0, pos=0, prev=None, next=None):
        self.valor = valor
        self.pos = pos
        self.prev = prev
        self.next = next

# a1) Busca por indice
def busca_por_indice(p, k):
    atual = p
    while atual:
        if atual.pos == k:
            return atual.valor
        if atual.pos > k:
            break
        atual = atual.next
    return 0

# a2) Busca por valor
def busca_por_valor(p, x):
    atual = p
    while atual:
        if atual.valor == x:
            return atual.pos
        atual = atual.next
    return -1

# a3) Atualizacao
def atualizacao(p, x, k):
    atual = p
    while atual and atual.pos < k:
        atual = atual.next

    if atual and atual.pos == k:
        if x != 0:
            atual.valor = x
        else:
            if atual.prev:
                atual.prev.next = atual.next
            else:
                p = atual.next
            if atual.next:
                atual.next.prev = atual.prev
        return p

    if x != 0:
        novo = NodeEsparso(x, k)
        if not p:
            return novo
        if atual == p:
            novo.next = p
            p.prev = novo
            return novo
        elif not atual:
            fim = p
            while fim.next:
                fim = fim.next
            fim.next = novo
            novo.prev = fim
        else:
            novo.next = atual
            novo.prev = atual.prev
            atual.prev.next = novo
            atual.prev = novo

    return p

# b) Analise de tempo
# As tres operacoes percorrem a lista encadeada no maximo uma vez.
# O tempo e O(k_nos), sendo k_nos a quantidade de elementos nao-nulos.