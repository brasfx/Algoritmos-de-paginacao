def NUF(moldura, processo, paginas):
    lista = []
    uso = []
    menos = 0
    pos = 0
    troca = 0
    for pagina in paginas:
        found = 0
        for i in range(len(lista)):
            if lista[i]==pagina:
                found = 1
                uso[i] = uso[i] + 1
        if len(lista)<moldura and found ==0:
            lista.append(pagina)
            uso.append(0)
            troca = troca + 1
        elif len(lista)==moldura and found == 0:
            menos = uso[0]
            pos = 0
            for i in range(len(lista)):
                if uso[i] < menos:
                    menos = uso[i]
                    pos = i
            uso[pos]=0
            lista[pos] = pagina
            troca = troca + 1
        #print(lista)
        #print(uso)


    return troca