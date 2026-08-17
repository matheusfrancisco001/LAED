class NodeEsparso:
    def __init__(self, valor=0, pos=0, prev=None, next=None):
        self.valor = valor
        self.pos = pos
        self.prev = prev
        self.next = next

# a) Algoritmo
def construir_esparso(V):
    p = None
    ultimo = None

    for i in range(len(V)):
        if V[i] != 0:
            novo = NodeEsparso(V[i], i)
            if not p:
                p = novo
                ultimo = novo
            else:
                ultimo.next = novo
                novo.prev = ultimo
                ultimo = novo

    return p

# b) Analise de tempo
# Percorre todas as posicoes do vetor V de tamanho m criando os nos nao nulos.
# O tempo e O(m), onde m e o tamanho do vetor original.