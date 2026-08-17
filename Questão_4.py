# a) Estrutura do no
# Cada no armazena:
# - val: o valor do elemento inserido
# - min_atual: o menor valor presente na pilha ate aquele nivel
# - next: ponteiro para o proximo no abaixo dele

class NodeMin:
    def __init__(self, val, min_atual, next=None):
        self.val = val
        self.min_atual = min_atual
        self.next = next

# b) Pseudocodigos O(1)
class PilhaMin:
    def __init__(self):
        self.topo = None

    def push(self, x):
        if self.topo is None:
            menor = x
        else:
            menor = min(x, self.topo.min_atual)
        self.topo = NodeMin(x, menor, self.topo)

    def pop(self):
        if self.topo is None:
            return None
        removido = self.topo
        self.topo = self.topo.next
        return removido.val

    def get_min(self):
        if self.topo is None:
            return None
        return self.topo.min_atual

# c) Trace da sequencia
# 1. Push(5): topo -> [val: 5, min: 5]
# 2. Push(3): topo -> [val: 3, min: 3] -> [val: 5, min: 5]
# 3. Push(7): topo -> [val: 7, min: 3] -> [val: 3, min: 3] -> [val: 5, min: 5]
# 4. Push(1): topo -> [val: 1, min: 1] -> [val: 7, min: 3] -> [val: 3, min: 3] -> [val: 5, min: 5]
# 5. Pop(): remove valor 1 | topo -> [val: 7, min: 3] -> [val: 3, min: 3] -> [val: 5, min: 5]
# 6. Min(): retorna 3

# d) Custo extra de memoria
# O custo extra e de exatamente 1 campo inteiro por no (min_atual).
# Em notacao assintotica, o custo de espaco extra total e O(n).