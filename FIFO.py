def FIFO(count_moldura, processos, paginas):
    miss = 0

    molduras = []

    for pag in paginas:
        if pag not in molduras:
            miss += 1

            if len(molduras) == count_moldura:
                molduras.pop(0)

            molduras.append(pag)

    return miss
