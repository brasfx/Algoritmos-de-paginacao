from random import randint


def readfile():  # retorna uma matriz de strings para representar o arquivo de processos
    result = []
    #nome_do_arquivo = input('Digite o nome do arquivo:\n')
    proc = open('entrada.txt', 'r')
    proc = (proc.read()).splitlines()
    for line in proc:
        line = line.split("|")
        result.append(line)
    return (result)


def tratamento(arquivo):
    for element in arquivo:  # converte as strings de numeros da lista em inteiros
        for it in range(0, 3):
            element[it] = element[it].replace(' ', ',')
            element[it] = eval(element[it])
    return arquivo

def FIFO(moldura, processo, paginas):
    print("teste")
def MRU(moldura, processo, paginas):
    print("teste")
def NUF(moldura, processo, paginas):
    print("teste")


saida = tratamento(readfile())
for line in saida:
    print(line)
    for data in line:
        print(data)