from random import randint
from FIFO import FIFO
from MRU import MRU
from NUF import NUF
from tratamento import tratamento,readfile





saida = tratamento(readfile())
for line in saida:
    print(line)
    for data in line:
        print(data)
        FIFO(1,1,1)