class TrieNode:
    def __init__(self, key):
        self.key = key
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def inserir(self, word):
        node = self.root
        for i in range(len(word)):
            char = word[i]
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    def procurar(self, word):
        node = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def remover(self, word):
        def _remover(node, word, depth=0):
            if depth == len(word):
                if node.is_end:
                    node.is_end = False
                    if not node.children:
                        return True
                return False
            
            char = word[depth]
            if char not in node.children:
                return False
            
            should_delete_node = _remover(node.children[char], word, depth+1)
            if should_delete_node:
                del node.children[char]
                if not node.children and not node.is_end:
                    return True
            
            return False
        
        _remover(self.root, word)

tree = Trie()
tree.inserir('hello')
tree.inserir('world')
tree.inserir('vinicius')
tree.inserir('vinick')
tree.inserir('vanessa')
tree.inserir('vanderson')


print(tree.procurar('vinicius'))  # True
print(tree.procurar('vanessa'))  # True
print(tree.procurar('vanderson'))  # True
print(tree.procurar('hello'))  # True
# print(tree.search('vanderberg')) #False
tree.remover('hello')
print(tree.procurar('hello'))  # False
tree.remover('vanderson')
print(tree.procurar('vanderson'))  # True
print(tree.procurar('vanessa'))  # True