from random import randint
from FIFO import FIFO
from MRU import MRU
from NUF import NUF
from tratamento import tratamento, readfile


saida = tratamento(readfile())
for line in saida:
    print(FIFO(line[0],line[1],line[2]),"|",MRU(line[0],line[1],line[2]))

