class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# a) Estado apos Push(99) e Push(3)
# Estado inicial: topo -> 42 -> 17 -> 5 -> None
# Apos Push(99):  topo -> 99 -> 42 -> 17 -> 5 -> None
# Apos Push(3):   topo -> 3 -> 99 -> 42 -> 17 -> 5 -> None

def push(topo, val):
    return Node(val, topo)

# b) Dois Pops a partir de (a)
# Primeiro Pop: remove o valor 3
# Pilha fica: topo -> 99 -> 42 -> 17 -> 5 -> None
# Segundo Pop: remove o valor 99
# Pilha final: topo -> 42 -> 17 -> 5 -> None

def pop(topo):
    if topo is None:
        return None, None
    removido = topo
    topo = topo.next
    removido.next = None
    return topo, removido.val

# c) Justificativa
# O no precisa ser guardado em variavel auxiliar para nao perder a referencia do proximo elemento (topo.next).
# Se a memoria do no fosse liberada antes de atualizar topo, o ponteiro de encadeamento seria destruido,
# impedindo o acesso ao restante da pilha e causando perda de referencia ou comportamento indefinido.