class Node:
    def __init__(self, val="", next=None):
        self.val = val
        self.next = next

# a) Algoritmo
def verificar_balanceamento(expr):
    pares = {')': '(', ']': '[', '}': '{'}
    topo = None

    for i in range(len(expr)):
        c = expr[i]
        if c in "({[":
            topo = Node(c, topo)
        elif c in ")}]":
            if topo is None:
                return False, f"Erro na posicao {i}: fechador '{c}' sem abridor correspondente"
            if topo.val != pares[c]:
                return False, f"Erro na posicao {i}: fechador '{c}' nao corresponde ao abridor '{topo.val}'"
            topo = topo.next

    if topo is not None:
        return False, "Erro: existem delimitadores abertos que nao foram fechados"

    return True, "Valida"

# b) Analise de complexidade
# Tempo: O(n), varre a string de tamanho n processando cada caractere em O(1).
# Espaco: O(n) no pior caso (quando todos os delimitadores sao de abertura).

# c) Aplicacao nas cadeias
# 1. ({[]}) -> Valida
# 2. ({[)}] -> Invalida (Posicao 3: fecha ')' quando o topo esperava fechar ']')
# 3. ({[]}[()]{}) -> Valida