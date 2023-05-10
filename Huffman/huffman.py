import os
from time import time

class Node: #Declaração de variáveis para criar os nós
    height = 0 #Declarada como int
    symbol = "" #Variável vazia
    encoding = ""
    visited = False #Variável Booleana
    parent = -1 #Comprimento de 0 a -1, a variável toda

class Huffman: #Declaração de variáveis para a criação da árvore de Huffman
    Tree = None #Retornar árvore
    Root = None #Retornar raiz
    Nodes = [] #Array
    freq = {} #Bloco, instâcia do método
    dictEncoder = {}

    #1
    def __init__(self, symbols): #Inicializamos as funções com os atributos que vão ser utilizados
        self.initNodes(symbols) #Retorna Valores
        self.buildTree()
        self.buildDictionary()

    #2
    def initNodes(self, freq): #Criamos os nós com suas respectivas probabilidades
        for symbol in freq:
            node = Node() #Inicializamos o nó
            node.symbol = symbol
            node.height = freq[symbol] #Colocamos um peso/frequência para cada símbolo ou letra
            node.visited = False #Variável que não é fixa, que vai mudar
            self.Nodes.append(node) #Criamos uma lista para cada nó criado
            self.freq[symbol] = freq[symbol] #Estabelece para cada peso um símbolo

    #3
    def buildTree(self): #Realizamos as operações de acordo com as regras para a construção da árvore de Huffman
        indexMin1 = self.getNodeWithMinimumFreq() #Buscamos o primeiro número de menor peso
        indexMin2 = self.getNodeWithMinimumFreq() #Buscamos o segundo número de menor peso

        while indexMin1 != -1 and indexMin2 != -1: #(!= o valor será verdadeiro se as duas variáveis forem diferentes)
            node = Node()
            node.symbol = "." #Chama o símbolo digitado para que forneça o resultado
            node.encoding = ""
            #Chamamos os pesos mínimos
            freq1 = self.Nodes[indexMin1].height
            freq2 = self.Nodes[indexMin2].height
            node.height = freq1 + freq2 #Somamos os pesos
            node.visited = False #False é igual a 1
            node.parent = -1 #Restando a probabilidade -1
            self.Nodes.append(node)
            self.Nodes[indexMin1].parent = len(self.Nodes) - 1 #Lista a cadeia que queremos medir
            self.Nodes[indexMin2].parent = len(self.Nodes) - 1

            #Regra: dígito 1 para o símbolo de maior peso e 0 para o menor
            if freq1 >= freq2:
                self.Nodes[indexMin1].encoding = "1"
                self.Nodes[indexMin2].encoding = "0"
            else:
                self.Nodes[indexMin1].encoding = "0"
                self.Nodes[indexMin2].encoding = "1"

            indexMin1 = self.getNodeWithMinimumFreq()
            indexMin2 = self.getNodeWithMinimumFreq()

    #4
    def getNodeWithMinimumFreq(self): #Realizamos uma comparação para obter o nó de menor peso
        minFreq = 1 #O menor peso não pode ser menor que 1
        indexMin = -1 #Indice para subtrair do peso

        for index in range(0, len(self.Nodes)): #Index é o número do peso
            if(self.Nodes[index].height < minFreq and (not self.Nodes[index].visited)): #Se o index é menor que 1 é falso
                minFreq = self.Nodes[index].height
                indexMin = index
        #(!= diferente de)
        if indexMin != -1:
            self.Nodes[indexMin].visited = True

        return indexMin

    #5
    def showSymbolEncoding(self, symbol): #Designamos um código binário a cada símbolo resultando na árvore de Huffman
        found = False
        index = 0
        encoding = "" #Reflejara o resultado

        for i in range(0, len(self.Nodes)):
            if self.Nodes[i].symbol == symbol: #Procedimento de como designar o código binário
                found = True
                index = i
                break

        if found:
            while index != -1: #Se found é verdadeiro enquanto index é diferente de -1 guardamos a codificação e mostramos o resultado
                encoding = "%s%s" % (self.Nodes[index].encoding, encoding)
                index = self.Nodes[index].parent
        else:
            encoding = "simbolo desconhecido"

        return encoding

    #6
    def buildDictionary(self): #Criamos um dicionário, guardamos todos os símbolos com seus respectivos códigos binários
                               #Resultando na árvore de Huffman
        for symbol in self.freq:
            encoding = self.showSymbolEncoding(symbol)
            self.dictEncoder[symbol] = encoding

    #7
    def encode(self, plain): #Agrupa os códigos binários codificados de acordo com a mensagem escrita no console
        encoded = ""
        for symbol in plain:
            encoded = "%s%s" % (encoded, self.dictEncoder[symbol])

        return encoded

    #Decodificação
    def decode(self, encoded): #Recebe a cadeia de código binário enviado pelo emissor para decodificar
        index = 0
        decoded = ""

        while index < len(encoded): #Enquanto medimos o comprimento da parte codificada
            found = False #Estabalecemos uma variável
            aux = encoded[index:] #Busca em cada parte codificada um símbolo
                                  
            for symbol in self.freq:
                if aux.startswith(self.dictEncoder[symbol]): #Cadeia é verificada se é verdadeira ou falsa. 
                    decoded = "%s%s" % (decoded, symbol) #Parte decodificada
                    index = index + len(self.dictEncoder[symbol]) #Busca para cada símbolo uma probabilidade
                    break

        return decoded

#Mensagem para Codificar
if __name__ == "__main__":
    mensagem = input("Escreva uma palavra ou um texto(string): ")
    print("\n\nTotal de simbolos: \n\n %s" % (len(mensagem)))
    simbolos = ''
    peso = []
    msg = mensagem
    d=0

    for i in mensagem:
        if i in msg:
            simbolos+=i
            peso.append(int(int(msg.count(i))/int(len(mensagem))))
            msg = msg.replace(i, '')
            d+=1

    symbols = dict(zip(simbolos, peso)) #Função para chamar o símbolo e o seu peso
    print("\n\nSimbolos comprimidos: \n\n", d) #Imprime a quantidade de símbolos que contabiliza a função count (d)
    print("\n\nPeso de cada símbolo:\n\n", symbols)

    tempo_inicial = time() #Função para determinar o tempo do programa

    #Codificação dos Símbolos
    huffman = Huffman(symbols) #Chamamos a classe Huffman
    print("\n\nSimbolos codificados usando a arvore de huffman: \n\n")
    for symbol in symbols:
        print("Simbolo: %s; Codificacao: %s" % (symbol, huffman.showSymbolEncoding(symbol)))

    encoded = huffman.encode(mensagem) #Chama função após função para o procedimento de codificação (recursividade)
    print("\n\nMensagem que esta sendo codificada: \n\n%s" % (mensagem))
    print("\n\nCodificacao em bits: \n\n%s" % (encoded)) #Tamanho da mensagem em bits
    print("\n\nA quantidade de bits utilzada para codificar a string eh: \n\n%s" % (len(encoded)))

    data = encoded

    decoded = huffman.decode(data) #Chamamos as funções correspondentes e a mensagem codificada
    print("O codigo binario para decodificar eh: \n\n", data)
    print("\n\nA mensagem decodificada eh: \n\n %s" % (decoded)) #Imprime o resultado da variável decoded

#Mensagem para Decodificar
##if __name__ == "__main__":
##    codigo = input("Escreva o codigo binario: ")
##    
##    tempo_inicial = time() #Função para determinar o tempo do programa
##
##    #Decodificação dos Símbolos
##    
##    decoded = huffman.decode(codigo) #Chamamos as funções correspondentes e a mensagem codificada
##    print("\n\nTotal de simbolos: \n\n %s" % (len(decoded)))
##    print("\n\nA mensagem decodificada eh: \n\n %s" % (decoded)) #Imprime o resultado da variável decoded

os._exit(0)