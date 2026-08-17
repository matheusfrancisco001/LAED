class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

# a) Inserir 7 e 11
# Estado inicial: inicio -> 8 -> 15 -> 23 <- fim
# Apos Enqueue(7):  inicio -> 8 -> 15 -> 23 -> 7 <- fim
# Apos Enqueue(11): inicio -> 8 -> 15 -> 23 -> 7 -> 11 <- fim

def enqueue(fila, val):
    novo = Node(val)
    if not fila.inicio:
        fila.inicio = novo
        fila.fim = novo
    else:
        fila.fim.next = novo
        fila.fim = novo

# b) Dois Dequeue a partir de (a)
# Primeiro Dequeue: remove 8
# Segundo Dequeue: remove 15
# Estado resultante: inicio -> 23 -> 7 -> 11 <- fim

def dequeue(fila):
    if not fila.inicio:
        return None
    removido = fila.inicio
    fila.inicio = fila.inicio.next
    if fila.inicio is None:
        fila.fim = None
    return removido.val

# c) Esvaziamento da fila
# Quando a fila esvazia (inicio vira None), o ponteiro fim deve obrigatoriamente ser setado para None tambem.
# Se apenas inicio for zerado e fim continuar apontando para o no removido, teremos um ponteiro pendente (dangling pointer).
# Isso quebraria futuras insercoes, pois a condicao de fila vazia ficaria inconsistente.