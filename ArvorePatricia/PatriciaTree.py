#procedimento utilizado para comparar duas palavras e
#localizar a posição em que os dígitos ese diferenciam
def get_intersection(word_one, word_two):

    """
    Busca o ponto onde duas strings se diferenciam
    :param str word_one:
    :param str word_two:
    :return int:
    """
    for i in range(len(word_one)):

        if len(word_two) > i:

            if word_one[i] != word_two[i]: return i

#Estrutura de um nó em uma Arvore Patricia
class Node:
    #procedimento que definine a estrutura básica de um nó.
    def __init__(self, position, value, radix):

        """
        Unidade basica
        :param int position:
        :param str value:
        :param str radix:
        """

        self.children = [None, None] #valores do campo X e Y
        #dos nós filhos.

        self.radix = radix #trecho do código ou palavra que
        #não há diferenciação entre as chaves.
        self.position = position #referente ao campo X
        #(posição a ser comparada).
        self.value = ord(value) #referente ao compo Y
        #(caractere a ser comparado).
        #A função ord() altera um caractere definido para um inteiro.

    #procedimento que percorre os nós na arvore.
    def get(self, word):

        if word[:self.position] != self.radix or len(word) <= self.position: return 0

        value = ord(word[self.position])

        if value <= self.value:

            #print("Esquerda!")
            return self.children[0]

        #print("Direita!")
        return self.children[1]

    #procedimento para exibir nós derivados de outros nós.
    def get_derivatives(self):

        derivatives = []

        for child in self.children:

            if type(child) == str: derivatives.append(child[:-1])

            else: derivatives += child.derivates()

        return derivatives

    #procedimento para fazer a representação dos campos X e Y do nó.
    def __repr__(self):

        return "[{}|{}]".format(self.position, chr(self.value))

#Estrutura de uma Arvore Patricia
class PatriciaTree:

    def __init__(self, root=None):

        """
        Inicia a árvore
        :param str root:
        """

        if type(root) == str:
            root += '$'

        self.root = root

    def insert(self, word):

        """
        Insere uma string na árvore
        :param str word:
        :return None:
        """

        # print("Inserindo %s" % word)

        #verifica se a palavra já existe na arvore, existindo não faz a inserção.
        if self.check(word):
            raise ValueError(f"The word {word} has already been inserted.")

        word += '$'

        if self.root is None:
            self.root = word
            return

        parent = None
        node = self.root

        while True:

            # Caso nó folha

            if type(node) == str:

                position = get_intersection(word, node)

                # Caso nó folha seja root também

                if parent is None:

                    elements = sorted([(ord(word[position]), word), (ord(node[position]), node)])
                    # print(elements)
                    self.root = Node(position, chr(elements[0][0]), elements[0][1][:position])

                    self.root.children = [element[1] for element in elements]

                    # print(self.root)
                    return


                # CASE: default (caso contrário)

                else:

                    side = parent.children.index(node)

                    # print(position)

                    elements = sorted([(ord(word[position]), word), (ord(node[position]), node)])

                    # parent.children[side] = Node(position, elements[0][position], elements[0][:position])
                    parent.children[side] = Node(position, chr(elements[0][0]), elements[0][1][:position])
                    parent.children[side].children = [element[1] for element in elements]

                    # print(parent.children[side])
                    return

            else: #se o tipo da variável nó não é uma string.

                next_node = node.get(word)

                # Caso radix não combina

                if not next_node:

                    position = get_intersection(word, node.radix)

                    elements = sorted([(ord(word[position]), word), (ord(node.radix[position]), node)])

                    # Caso root

                    if parent is None:

                        self.root = Node(position, chr(elements[0][0]), word[:position])

                        self.root.children = [element[1] for element in elements]

                        return

                    else:

                        side = parent.children.index(node)
                        # print(side, parent.children)
                        # print(elements)
                        parent.children[side] = Node(position, chr(elements[0][0]), word[:position])
                        parent.children[side].children = [element[1] for element in elements]

                        return

                # Base de iteração

                else:

                    parent = node
                    node = next_node

    #procedimento para fazer a busca de uma palavra (chave).
    def check(self, word):

        if self.root is None:
            return False

        word += '$'

        node = self.root

        while 1:

            if type(node) == str:
                return node == word

            next_node = node.get(word)
            # print(next_node)
            if next_node:

                node = next_node

            else:

                return False
            
    #procedimento para fazer a remoção de uma palavra (chave).
    def remove(self, word):

        #faz a verificacao se a palavra (chave) está na arvore.
        if not self.check(word):
            raise ValueError(f"Word {word} not found.")

        word += '$' #adiciona esse símbolo para os nós
        #que não tem o final de uma chave como nó folha

        grandparent = None
        parent = None
        node = self.root

        #critério 2
        while 1:

            if type(node) == str:

                if parent is None:

                    self.root = None
                    return

                else:

                    parent.children.remove(node)
                    new_successor = parent.children[0]

                    if grandparent is None:

                        self.root = new_successor
                        del parent

                        return

                    else:

                        index = grandparent.children.index(parent)
                        grandparent.children[index] = new_successor
                        del parent

                        return

            else:

                next_node = node.get(word)

                if parent is None:

                    parent = node
                    node = next_node

                else:

                    grandparent = parent
                    parent = node
                    node = next_node

    def get_derivatives(self, radix):

        """
        Exibe folhas derivadas de determinado radix
        :param str radix:
        :return str[]:
        """

        size = len(radix)
        node = self.root

        #exibe os nós folhas derivados de radix que iniciam por 1 e por 0
        #de acordo com o menor tamanho comum do radix existente entre
        #duas ou mais chaves na arvore.
        while 1:

            if type(node) == str:

                if node[:size] == radix:

                    return [node[:-1]]

                else:

                    return []

            else:

                if node.radix == radix or node.radix[:size] == radix:
                    return node.get_derivatives()

                next_node = node.get(radix)

                if next_node:
                    node = next_node
                else:
                    return []

    #procedimento para verificar se a arvore está vazia ou não.
    def __repr__(self):
        if self.root is None:
            return "<Empty PatriciaTree object>"
        else:
            return "<PatriciaTree object>\n" + str(self.root)

if __name__ == '__main__':

    patricia = PatriciaTree()

    print("Inserindo chaves...\n")
    
    patricia.insert('000100')
    patricia.insert('010100')
    patricia.insert('000010')
    patricia.insert('100100')
    patricia.insert('001001')
    patricia.insert('001100')
    patricia.insert('101000')
    patricia.insert('101010')

    print("Desenhando Arvore Patricia...\n")
    
    print(patricia.root)
    print(patricia.root.children)
    print(patricia.root.children[0].children + patricia.root.children[1].children)
    print(patricia.root.children[0].children[0].children +
          [""] +
          [""] +
          [""] +
          [""] +
          patricia.root.children[1].children[1].children)
    print(patricia.root.children[0].children[0].children[0].children +
          patricia.root.children[0].children[0].children[1].children +
          [""] +
          [""] +
          [""] +
          [""] +
          [""] +
          [""] +
          [""] +
          [""] +
          [""])

    print("\nBuscando a chave 001001:\n")
    if(patricia.check('001001') == True):
        print("A chave foi encontrada.\n")
    else:
        print("A chave nao foi encontrada.\n")      
    
    print("Removendo chave(s)...")

    patricia.remove('001001')
   
    if(patricia.check('001001') == True):
        print("A chave 001001 foi encontrada.\n")
    else:
        print("A chave 001001 nao foi encontrada.\n")

    print(patricia.get_derivatives('010'))