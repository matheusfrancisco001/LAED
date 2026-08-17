class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# a) Algoritmo
def tem_repetido(p):
    vistos = set()
    atual = p
    while atual:
        if atual.val in vistos:
            return "Sim"
        vistos.add(atual.val)
        atual = atual.next
    return "Nao"

# b) Analise de tempo
# Percorre a lista buscando no conjunto a cada no visitado.
# Como a busca no set e O(1) em media, o tempo total e O(n).