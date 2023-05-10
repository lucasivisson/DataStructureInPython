##import networkx as nx
##import matplotlib.pyplot as plt
##
##G = nx.Graph()
## Biblioteca para plotar grafos de uma árvore quaisquer (Trie, ABB, AVP, AVL e etc).

#Estrutura de Dados para definir um Nó
class Node:
    def __init__(self, key=None, data=None):
    #procedimento para inicializar um nó com chave(dígito) e dados sem valor
        self.key = key
        self.data = data
        self.children = dict() #função para agregar um par de informações
    
    def addChild(self, key, data=None):
    #procedimento para adicionar um nó filho a um nó
        if not isinstance(key, Node):
            self.children[key] = Node(key, data)
        else:
            self.children[key.label] = key

#Estrutura de Dados para definir uma Trie
class Trie:
    def __init__(self):
    #procedimento para definir um nó como a raiz
        self.head = Node()
    
    def insert(self, word):
    #procedimento para inserção de nós na Trie
        current_node = self.head #começa a busca pela raiz da árvore para saber se vai ser preciso inserir nós (dígitos) ou não na árvore.
        word_finished = True

        #percorre dígito por dígito da chave até encontrar um dígito diferente da chave em relação aos dígitos armazenados na árvore.
        
        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                word_finished = False
                break

        #acrescenta os nós com os dígitos da chave que não existe na árvore.
        
        if not word_finished:
            while i < len(word):
                current_node.addChild(word[i])
                current_node = current_node.children[word[i]]
                i += 1

        #O último nó percorrido armazena a informação completa da chave. 
        
        current_node.data = word

        print("A palavra ", word, " foi inserida\n")
    
    def insert_words(self, words):
    #procedimento para inserir várias palavras ou códigos (chaves).
        for word in words.split():
            self.insert(word)
       
    def search(self, word):
    #procedimento para fazer a busca de uma chave em uma Trie.
        if word == '':
            return False
        if word == None:
            raise ValueError('Trie.search precisa de uma string valida.')

        current_node = self.head #começa a busca pela raiz da árvore.
        exists = True

        #percorre cada dígito na árvore e compara com os dígitos da chave buscada.
        
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                exists = False
                break

        #se a chave existir na árvore, a chave é informada.
        
        if exists:
            if current_node.data == None:
                exists = False
        
        return exists
        
    def remove(self, word):
    #procedimento para fazer a remoção dos nós que não compõem outra(s) chave(s)
        if word == '':
            return False
        if word == None:
            raise ValueError('Trie.search precisa de uma string valida')

        current_node = self.head #começa a busca pela raiz da árvore para saber qual ou quais nós serão removidos da árvore.
        exists = True

        #percorre cada dígito na árvore e compara com os dígitos da chave buscada.
        
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                exists = False
                break

        #se a chave existir na árvore, o nó atual é marcado como nulo até os nós referentes à chave serem eliminados.
        #sendo removidos somente os nós cujos os dígitos não compõem nenhuma outra chave existente na árvore.
            
        if exists:
            current_node.data = None
            print("A palavra ", word, " foi removida.\n")

if __name__ == '__main__':

    trie = Trie()
    words = 'foi fora fui vai ver vi viu vimos veremos'

    print("Inserindo as palavras: ", words)

    trie.insert_words(words)

    print("Busca: ver, veremos e fora\n")
    if(trie.search('ver') == True):
        print("A palavra foi encontrada.\n")
    else:
        print("A palavra nao foi encontrada.\n")      

    if(trie.search('veremos') == True):
        print("A palavra foi encontrada.\n")
    else:
        print("A palavra nao foi encontrada.\n")  

    if(trie.search('fora') == True):
        print("A palavra foi encontrada.\n")
    else:
        print("A palavra nao foi encontrada.\n")

    print("Remocao: fora\n")
    
    trie.remove('fora')

    print("Busca: fora\n")
    
    if(trie.search('fora') == True):
        print("A palavra foi encontrada.\n")
    else:
        print("A palavra nao foi encontrada.\n")

    print("Insercao: fora\n")

    trie.insert('fora')

    print("Busca: fora\n")

    if(trie.search('fora') == True):
        print("A palavra foi encontrada.\n")
    else:
        print("A palavra nao foi encontrada.\n")  