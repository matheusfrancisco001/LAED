# a) Contra-exemplo com Pilhas no lugar de Filas
# O Radix Sort exige algoritmo estavel para preservar a ordem do digito anterior.
# Se usarmos pilhas, os elementos com o mesmo digito saem na ordem invertida (LIFO),
# destruindo a ordenacao relativa conquistada nos passos anteriores.
# Exemplo: Ordenando [12, 22] pelo digito menos significativo (2):
# Ambos vao para a estrutura do digito 2.
# Com Fila (FIFO): coleta sai [12, 22] (mantem a ordem).
# Com Pilha (LIFO): coleta sai [22, 12] (inverteu a ordem relativa).

# b) Trace para: [481, 329, 143, 612, 937, 480, 256]
#
# Passagem 1 (Unidades):
# Filas: 0:[480], 1:[481], 2:[612], 3:[143], 6:[256], 7:[937], 9:[329]
# Apos coleta 1: [480, 481, 612, 143, 256, 937, 329]
#
# Passagem 2 (Dezenas):
# Filas: 1:[612], 2:[329], 3:[937], 4:[143], 5:[256], 8:[480, 481]
# Apos coleta 2: [612, 329, 937, 143, 256, 480, 481]
#
# Passagem 3 (Centenas):
# Filas: 1:[143], 2:[256], 3:[329], 4:[480, 481], 6:[612], 9:[937]
# Sequencia final: [143, 256, 329, 480, 481, 612, 937]

# c) Complexidade
# Para n strings de tamanho d sobre alfabeto de tamanho k:
# Tempo Radix Sort: O(d * (n + k)).
# Comparacao com Merge Sort:
# O Merge Sort faz O(n log n) comparacoes. Como comparar duas strings de tamanho d custa O(d),
# o Merge Sort leva O(d * n log n).
# Portanto, para valores moderados de k e d, o Radix Sort e mais eficiente que o Merge Sort.