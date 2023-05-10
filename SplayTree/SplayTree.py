# Vinicius Vieira Carneiro 
# Mat: 1509015

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.pai = None
        self.filhoEsq = None
        self.filhoDir = None


class SplayTree:
    def __init__(self):
        self.root = None

    def inserir(self, n):
        y = None
        temp = self.root
        while temp != None:
            y = temp
            if n.data < temp.data:
                temp = temp.filhoEsq
            else:
                temp = temp.filhoDir

        n.pai = y

        if y == None:  # newly added node is root
            self.root = n
        elif n.data < y.data:
            y.filhoEsq = n
        else:
            y.filhoDir = n

        self.splay(n)

    def rotacaoEsq(self, x):
        y = x.filhoDir
        x.filhoDir = y.filhoEsq
        if y.filhoEsq != None:
            y.filhoEsq.pai = x

        y.pai = x.pai
        # x é root
        if x.pai == None:
            self.root = y
        # x é filhoEsq
        elif x == x.pai.filhoEsq:
            x.pai.filhoEsq = y
        # x é filhoDir
        else:
            x.pai.filhoDir = y

        y.filhoEsq = x
        x.pai = y

    def rotacaoDir(self, x):
        y = x.filhoEsq
        x.filhoEsq = y.filhoDir
        if y.filhoDir != None:
            y.filhoDir.pai = x

        y.pai = x.pai
        # x é root
        if x.pai == None:
            self.root = y
        # x is filhoDir child
        elif x == x.pai.filhoDir:
            x.pai.filhoDir = y
        # x is filhoEsq child
        else:
            x.pai.filhoEsq = y

        y.filhoDir = x
        x.pai = y

    def splay(self, n):
        # no não é o root
        while n.pai != None:
            # rotação simples
            if n.pai == self.root:
                # zig direita
                if n == n.pai.filhoEsq:
                    self.rotacaoDir(n.pai)
                # zig esquerda
                else:
                    self.rotacaoEsq(n.pai)
            # rotação dupla
            else:
                p = n.pai
                avo = p.pai

                # zigzig direita
                if n.pai.filhoEsq == n and p.pai.filhoEsq == p:  # ambos são filhoEsq
                    self.rotacaoDir(avo)
                    self.rotacaoDir(p)
                # zigzig esquerda
                elif n.pai.filhoDir == n and p.pai.filhoDir == p:  # ambos são filhoDir
                    self.rotacaoEsq(avo)
                    self.rotacaoEsq(p)
                # zigzag equerda direita
                elif n.pai.filhoDir == n and p.pai.filhoEsq == p:
                    self.rotacaoEsq(p)
                    self.rotacaoDir(avo)
                # zigzag direita esquerda
                elif n.pai.filhoEsq == n and p.pai.filhoDir == p:
                    self.rotacaoDir(p)
                    self.rotacaoEsq(avo)
    
    def remover(self, n, x):
        no = self.procurar(n, x)
        if no == None:
            return None
        if no.filhoEsq is None and no.filhoDir is None:
            if no == self.root:
                self.root = None
            elif no.pai.filhoEsq == no:
                no.pai.filhoEsq = None
            else:
                no.pai.filhoDir = None
        #caso o no tenha um filho
        elif no.filhoEsq is None:
            if no == self.root:
                self.root = no.filhoDir
                no.filhoDir.pai = None
        elif no.filhoDir is None:
            if no == self.root:
                self.root = no.filhoEsq
                no.filhoEsq.pai = None
        #caso o no tenha doi filhos
        else:
            sucessor = self.minimo(no.filhoDir)
            if sucessor.pai is not no:
                sucessor.pai.filhoEsq = sucessor.filhoDir
                if sucessor.filhoDir is not None:
                    sucessor.filhoDir.pai = sucessor.pai

                sucessor.filhoDir = no.filhoDir
                sucessor.filhoDir.pai = sucessor
            if sucessor.pai is no:
                self.root = sucessor
                sucessor.pai = None
            elif sucessor.pai.filhoEsq is no:
                no.pai.filhoDir = sucessor
                sucessor.pai = no.pai
        
            sucessor.filhoEsq = no.filhoEsq
            sucessor.filhoEsq.pai = sucessor

        self.splay(n.pai if no.pai is not None else no)       

    def minimo(self, n):
        while n.filhoEsq is not None:
            n = n.filhoEsq
        return n

    def procurar(self, n, x):
        if n is None:
            return None
        if x == n.data:
            self.splay(n)
            return n
        elif x < n.data:
            return self.procurar(n.filhoEsq, x)
        elif x > n.data:
            return self.procurar(n.filhoDir, x)
        else:
            return None

    def preOrdem(self, n):
        if n != None:
            print(n.data, end=' ')
            self.preOrdem(n.filhoEsq)
            self.preOrdem(n.filhoDir)

    def emOrdem(self, n):
        if n != None:
            self.emOrdem(n.filhoEsq)
            print(n.data, end=' ')
            self.emOrdem(n.filhoDir)

    def posOrdem(self, n):
        if n != None:
            self.posOrdem(n.filhoEsq)
            self.posOrdem(n.filhoDir)
            print(n.data, end=' ')

if __name__ == '__main__':
    tree = SplayTree()
    list = [TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(
        4), TreeNode(5), TreeNode(6), TreeNode(7), TreeNode(8)
        , TreeNode(9), TreeNode(10), TreeNode(11), TreeNode(12), TreeNode(13)]
    for no in list:
        tree.inserir(no)
    n1 = tree.procurar(tree.root, 3)
    print('valor encontrado ', n1.data)
    tree.remover(tree.root, 9)
    n2 = tree.procurar(tree.root, 9)
    print('valor encontrado ', n2.data)
    n3 = tree.procurar(tree.root, 1)
    print('valor encontrado ', n3.data)
    n4 = tree.procurar(tree.root, 5)
    print('valor encontrado ', n4.data)
    
    # tree.inserir(TreeNode(3))
    # tree.inserir(TreeNode(4))
    # tree.inserir(TreeNode(1))
    # tree.inserir(TreeNode(2))
    # tree.inserir(TreeNode(5))
    tree.remover(tree.root, 1)
    tree.remover(tree.root, 9)

    tree.preOrdem(tree.root)
    print()
    tree.emOrdem(tree.root)
    print()
    tree.posOrdem(tree.root)
    print()
