def FIFO(count_moldura, processos, paginas):
    miss = 0  # contador de trocas

    molduras = []  # array pra inserir as paginas

    for pag in paginas:
        if pag not in molduras:  # se a pagina não esta na moldura é incrementado o contador
            miss += 1

            if len(molduras) == count_moldura:  # se o tamanho das molduras for maximo
                molduras.pop(0)  # retira o primeiro elemento

            molduras.append(pag)  # adiciona nova pagina a moldura

    return miss
