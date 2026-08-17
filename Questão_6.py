class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# a) Pseudocodigos
class FilaDuasPilhas:
    def __init__(self):
        self.p1 = None  # Entrada
        self.p2 = None  # Saida

    def enqueue(self, x):
        self.p1 = Node(x, self.p1)

    def dequeue(self):
        if not self.p2:
            while self.p1:
                no = self.p1
                self.p1 = self.p1.next
                no.next = self.p2
                self.p2 = no

        if not self.p2:
            return None

        removido = self.p2
        self.p2 = self.p2.next
        return removido.val

# b) Custo amortizado O(1) pelo metodo do potencial
# Seja o potencial Phi = numero de elementos em p1.
# - Enqueue: Custo real = O(1). Variacao de potencial Delta_Phi = +1. Custo amortizado = 1 + 1 = O(1).
# - Dequeue quando p2 nao e vazia: Custo real = O(1). Delta_Phi = 0. Custo amortizado = O(1).
# - Dequeue quando p2 esta vazia: Seja k elementos em p1. Custo real = 2k (passar k elementos de p1 para p2).
#   Novo potencial Phi' = 0, entao Delta_Phi = -k.
#   Custo amortizado = 2k + (-k) = k - k + 1 = O(1).
# Portanto, a media por operacao e estritamente O(1).

# c) Preservacao da ordem FIFO
# Sim, preserva. A primeira pilha inverte a ordem de entrada (LIFO).
# Ao transferir todos os elementos de p1 para p2, a ordem e invertida novamente,
# restaurando a ordem de chegada original (FIFO).