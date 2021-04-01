def Otimo(moldura, processos, paginas):
    lista = []
    peso = []
    miss = 0
    indiceatual = 0
    maior = 0
    pos = 0
    for pagina in paginas:
        if pagina not in lista:
            miss = miss + 1
            if len(lista) < moldura:
                lista.append(pagina)
            else:
                for processo in range(len(lista)):
                    peso.append(0)
                    for prox in range(indiceatual+1, len(paginas)):
                        if paginas[prox] != lista[processo]:
                            peso[processo] = peso[processo] + 1
                        else:
                            break
                for p in range(len(peso)):
                    if peso[p] > maior:
                        maior = peso[p]
                        pos = p
                lista[pos] = pagina
                peso.clear()
                maior = 0
                pos = 0
        
        indiceatual = indiceatual + 1


    return miss
