
RED = "RED"
BLACK = "BLACK"
cores = [BLACK, RED]

class VPNode:
    def __init__(self, valor, cor, pai, esq = None, dir = None):
        assert isinstance(valor, int) # deve ser valor inteiro
        assert cor in cores
        self.valor = valor
        self.cor = cor
        self.pai = pai
        self.esq = esq
        self.dir = dir
        self.is_end = None
    
    # def __bool__(self):
    #     if self.valor == False:
    #         return False
    #     return True
    
    # def __repr__(self):
    #     if not self.esq and not self.dir:
    #         return f'Valor do Nó {self.valor} sua cor é {self.cor} \n e não tem filho com {self.pai.valor} como pai'
    #     elif self.esq and not self.dir:
    #         return f'Valor do Nó {self.valor} sua cor é {self.cor} \n tem filho {self.esq.valor} como filho esquerdo e pai {self.pai.valor} como pai'
    #     elif not self.esq and self.dir:
    #          return f'Valor do Nó {self.valor} sua cor é {self.cor} \n tem filho {self.dir.valor} como filho esquerdo e pai {self.pai.valor} como pai'
    #     else:
    #          return f'Valor do Nó {self.valor} e sua cor é {self.cor}.\ntem dois filhos, {self.esq.valor} e {self.dir.valor} como filho esquerso e direito, e pai {self.pai.valor}'
        

#Classe Rubro Negra

class VPTree:
    NIL_FOLHA = VPNode(valor = False, cor = BLACK, pai = None) # Cria-se um Nó inicial

    def __init__(self):
        self.root = VPTree.NIL_FOLHA
    
    def inserir(self, valor):
        novo = VPNode(valor = valor, cor = RED, pai = None, esq = VPTree.NIL_FOLHA, dir = VPTree.NIL_FOLHA)
        self._inserir(novo)
        self._inserir_finup(novo)

    def _inserir(self, novo):
        pai = None
        atual = self.root
        while atual != VPTree.NIL_FOLHA:
            pai = atual
            if novo.valor < atual.valor:
                atual = atual.esq
            else:
                atual = atual.dir
        novo.pai = pai
        if pai == None:
            self.root = novo
        elif novo.valor < pai.valor:
            pai.esq = novo
        else:
            pai.dir = novo
    
    def _inserir_finup(self, novo):
        if(novo.pai == None):
            novo.cor = BLACK
            return
        while novo.pai.cor == RED:
            if novo.pai == novo.pai.pai.esq: # pai é filho esquerdo 
                y = novo.pai.pai.dir
                if y.cor == RED:
                    novo.pai.cor = BLACK
                    y.cor = BLACK
                    novo.pai.pai.cor = RED
                    novo = novo.pai.pai
                else:
                    if novo == novo.pai.dir:
                        novo = novo.pai
                        self._rotate_esq(novo)
                    novo.pai.cor = BLACK
                    novo.pai.pai.cor = RED
                    self._rotate_dir(novo.pai.pai)
            else:
                y = novo.pai.pai.esq
                if y.cor == RED:
                    novo.pai.cor = BLACK
                    y.cor = BLACK
                    novo.pai.pai.cor = RED
                    novo = novo.pai.pai
                else:
                    if novo == novo.pai.esq:
                        novo = novo.pai
                        self._rotate_dir(novo)
                    novo.pai.cor = BLACK
                    novo.pai.pai.cor = RED
                    self._rotate_esq(novo.pai.pai)
            if(novo.pai == None):
                break
        self.root.cor = BLACK

    def _rotate_esq(self, n):
        y = n.dir
        n.dir = y.esq
        if y.esq != VPTree.NIL_FOLHA:
            y.esq.pai = n
        y.pai = n.pai
        if n.pai == None:
            self.root = y
        elif n == n.pai.esq:
            n.pai.esq = y
        else:
            n.pai.dir = y
        y.esq = n
        n.pai = y
    
    def _rotate_dir(self, n):
        y = n.esq
        n.esq = y.dir
        if y.dir != VPTree.NIL_FOLHA:
            y.dir.pai = n
        y.pai = n.pai
        if n.pai == None:
            self.root = y
        elif n == n.pai.dir:
            n.pai.dir = y
        else:
            n.pai.esq = y
        y.dir = n
        n.pai = y
    
    def search(self, valor):
        return self._search(self.root, valor)
    
    def _search(self, atual, valor):
        if atual == VPTree.NIL_FOLHA or valor == atual.valor:
            return atual
        if valor < atual.valor:
            return self._search(atual.esq, valor)
        else:
            return self._search(atual.dir, valor)
    
    def delete(self, valor):
        z = self.search(valor)
        if z == VPTree.NIL_FOLHA:
            return
        y = z
        y_original_cor = y.cor
        if z.esq == VPTree.NIL_FOLHA:
            n = z.dir
            self._transplant(z, z.dir)
        elif z.dir == VPTree.NIL_FOLHA:
            n = z.esq
            self._transplant(z, z.esq)
        else:
            y = self._tree_minimum(z.dir)
            y_original_cor = y.cor
            n = y.dir
            if y.pai == z:
                n.pai = y
            else:
                self._transplant(y, y.dir)
                y.dir = z.dir
                y.dir.pai = y
            self._transplant(z, y)
            y.esq = z.esq
            y.esq.pai = y
            y.cor = z.cor
        if y_original_cor == BLACK:
            self._delete_finup(n)
    
    def _delete_finup(self, n):
        while n != self.root and n.cor == BLACK:
            if n == n.pai.esq:
                w = n.pai.dir
                if w.cor == RED:
                    w.cor = BLACK
                    n.pai.cor = RED
                    self._rotate_esq(n.pai)
                    w = n.pai.dir
                if w.esq.cor == BLACK and w.dir.cor == BLACK:
                    w.cor = RED
                    n = n.pai
                else:
                    if w.dir.cor == BLACK:
                        w.esq.cor = BLACK
                        w.cor = RED
                        self._rotate_dir(w)
                        w = n.pai.dir
                    w.cor = n.pai.cor
                    n.pai.cor = BLACK
                    w.dir.cor = BLACK
                    self._rotate_esq(n.pai)
                    n = self.root
            else:
                w = n.pai.esq
                if w.cor == RED:
                    w.cor = BLACK
                    n.pai.cor = RED
                    self._rotate_dir(n.pai)
                    w = n.pai.esq
                if w.dir.cor == BLACK and w.esq.cor == BLACK:
                    w.cor = RED
                    n = n.pai
                else:
                    if w.esq.cor == BLACK:
                        w.dir.cor = BLACK
                        w.cor = RED
                        self._rotate_esq(w)
                        w = n.pai.esq
                    w.cor = n.pai.cor
                    n.pai.cor = BLACK
                    w.esq.cor = BLACK
                    self._rotate_dir(n.pai)
                    n = self.root
        n.cor = BLACK
    
    def _transplant(self, u, v):
        if u.pai == None:
            self.root = v
        elif u == u.pai.esq:
            u.pai.esq = v
        else:
            u.pai.dir = v
        v.pai = u.pai
    
    def _tree_minimum(self, atual): #retorna o menor valor da subarvore
        while atual.esq != VPTree.NIL_FOLHA:
            atual = atual.esq
        return atual
    
    def print_tree(self):
        self._print_tree(self.root)
    
    def _print_tree(self, atual):
        if atual != VPTree.NIL_FOLHA:
            self._print_tree(atual.esq)
            print(atual.valor)
            self._print_tree(atual.dir)

    def print_tree_color(self):
        self._print_tree_color(self.root)
    
    def _print_tree_color(self, atual):
        if atual != VPTree.NIL_FOLHA:
            self._print_tree_color(atual.esq)
            print(atual.valor, atual.cor)
            self._print_tree_color(atual.dir)
    
    def print_tree_level(self):
        self._print_tree_level(self.root)
    
    def _print_tree_level(self, atual):
        if atual != VPTree.NIL_FOLHA:
            print(atual.valor)
            self._print_tree_level(atual.esq)
            self._print_tree_level(atual.dir)
    
    def print_tree_level_color(self):
        self._print_tree_level_color(self.root)
    
    def _print_tree_level_color(self, atual):
        if atual != VPTree.NIL_FOLHA:
            print(atual.valor, atual.cor)
            self._print_tree_level_color(atual.esq)
            self._print_tree_level_color(atual.dir)


if __name__ == "__main__":
    arvore = VPTree()
    valores = [5, 3, 10, 20, 100, 40, 50, 80, 70, 55, 90]
    for valor in valores:
        arvore.inserir(valor)
    # arvore.print_tree_level_color()

    # arvore.delete(5)
    # arvore.print_tree_level_color()
    # arvore._tree_minimum(arvore.root)
    # arvore.print_tree_level_color()
    # valor = arvore.search(100)
    # print(valor.valor)
    arvore.print_tree_level()