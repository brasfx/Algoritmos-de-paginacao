from random import randint
from FIFO import FIFO
from MRU import MRU
from NUF import NUF
from tratamento import tratamento, readfile


saida = tratamento(readfile())
for line in saida:
    print(line)
    for data in line:
        print(data)
saida_FIFO = FIFO(9, 27, (10, 23, 15, 1, 27, 25, 5, 12, 10, 4, 20, 4, 13, 22, 24, 2, 17, 16, 8, 15, 9, 23, 9, 9, 14, 14, 16, 26, 16, 2, 10, 21, 22, 14, 7, 11, 4, 26,
                          14, 24, 16, 5, 6, 23, 15, 15, 3, 9, 23, 15, 26, 23, 3, 4, 22, 5, 4, 10, 14, 19, 24, 26, 8, 17, 21, 17, 10, 13, 21, 11, 17, 6, 9, 27, 2, 8, 17, 4, 14, 12, 2))
print('FIFO:', saida_FIFO)
