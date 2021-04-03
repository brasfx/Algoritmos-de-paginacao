<h1>Simulador de algoritmos de substituição de páginas na memória</h1>

<h2>Algoritmos utilizados:</h2>

FIFO (First In First Out)</br>
MRU (Menos usado recentemente)</br>
NUF (Não usado frequentemente)</br>
Ótimo</br>

<h2>Descrição do programa principal:</h2>

A aplicação principal (main.py) chama as funções de leitura de arquivo e tratamento a fim de receber a entrada do arquivo de texto. Então para cada linha deste arquivo os algoritmos FIFO, MRU e NUF são chamados e seus resultados recebidos, então são comparados e a saída é processada no cmd formatada da seguinte maneira:

Número de trocas de página no algoritmo FIFO|Número de trocas de página no algoritmo MRU|Número de trocas de página no algoritmo NUF|Número de trocas de página no algoritmo ótimo|nome do algoritmo com desempenho mais próximo do ótimo

Por exemplo: 44 | 49 | 48 | 31 | FIFO

Não é necessária nenhuma interação do usuário, o programa se encerra após calcular todas as linhas.

<h2>Descrição dos algortimos:</h2>

1.FIFO:
  First in First Out, caso a página não esteja nas molduras, um miss é contabilizado e a próxima página é inserida, caso o tamanho da lista de molduras for igual ao numero máximo de molduras, o primeiro a ser inserido é retirado antes de inserir a próxima página.

2.MRU:
  É efetuada um loop na lista de páginas e para cada página é efetuado uma procura na lista de molduras, se a página for encontrada o seu contador de uso é retornado a 0, se a página na moldura não for a necessária, seu contador é incrementado. Caso a página não seja encontrada na lista e o tamanho da lista for menor que o número máximo de molduras, a página é adicionada a memória, uma variável auxilidar de contador é adicionada a lista de usos e um miss(troca) é contabilizado. Caso a lista esteja cheia será procurado a página que passou a mais ciclos sem ser usada e ela será substituida, contabilizando um miss.

3.NUF:
  É efetuada um loop na lista de páginas e para cada página é efetuado uma procura na lista de molduras, se a página for encontrada o seu contador de uso é incrementado. Caso a página não seja encontrada na lista e o tamanho da lista for menor que o número máximo de molduras, a página é adicionada a memória, uma variável auxilidar de contador é adicionada a lista de usos e um miss(troca) é contabilizado. Caso a lista esteja cheia será procurado a página que menos foi acessada e ela será substituida, contabilizando um miss e o contador sendo zerado novamente para aquela posição.
  
4.Ótimo:
  É efetuada um loop na lista de páginas, caso a página não esteja na lista um miss é contabilizado, se a lista não estiver cheia a página é adicionada a lista. Caso a lista esteja cheia um loop irá percorrer a lista e para cada página na lista sera efetuado outro loop para verificar quando aquela página será usada novamente, um peso é dado a cada página, a pagina com o peso maior será a que irá demorar mais para ser acessada novamente. É verificado qual página tem o maior peso e esta página é substituída, a lista de pesos então é zerada. Ao fim do loop inicial o contador do indice atual é incrementado.
  
<h2>Execução do código:</h2>
Linux:</br>
1. No terminal digitar o caminho do arquivo</br>
2. python3 main.py
</br>
Windows:</br>
Abrir a pasta do código e executar a main.py
