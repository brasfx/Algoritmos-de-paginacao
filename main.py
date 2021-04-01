from FIFO import FIFO
from MRU import MRU
from NUF import NUF
from tratamento import tratamento, readfile


saida = tratamento(readfile())
nfu = 1000
otimo = 1000
for line in saida:
    fifo = FIFO(line[0], line[1], line[2])
    mru = MRU(line[0], line[1], line[2])
    #nfu = NUF(line[0],line[1],line[2])
    #otimo = Otimo(line[0],line[1],line[2])
    if fifo < mru <= nfu:
        menor = "FIFO"
    elif mru < fifo <= nfu:
        menor = "MRU"
    elif nfu < fifo <= mru:
        menor = "MUF"
    else:
        menor = "empate"
    print(fifo, "|", mru, "|", nfu, "|", otimo, "|", menor)
