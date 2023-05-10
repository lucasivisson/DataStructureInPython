from node import Node

class LinkedList:
  def __init__(self):
    self.head = None
    self._size = 0

  def append(self, elem):
    if self.head:
      # inserção quando a lista já possui elementos
      pointer = self.head
      while(pointer.next):
        pointer = pointer.next
      pointer.next = Node(elem)
    else:
      self.head = Node(elem)
    self._size += 1

  def __len__(self):
    # Sobrescreve a função len do python para a classe linkedList
    """Retorna o tamanho da lista"""
    return self._size

  def get(self, index):
    # list.get(5)
    pass

  def set(self, index, elem):
    # list.set(5, 6)
    pass

  # Python nos permite fazer sobrecarga de operador, no caso podemos sobrescrever as duas funções abaixo que são usadas pelo python para poder buscar um item ou setar um item usando a notação de colchete, mas nem toda linguagem permite essa sobrecarga do operador, caso a linguagem não permita, você terá que implementar as funções acima e utilizar a notação    list.get(6) ou list.set(5, 9)
  def __getitem__(self, index):
    # como estamos fazendo a sobrecarga de operador, podemos usar a notação a seguir agora: lista[6]
    pointer = self.head
    for i in range(index):
      if pointer:
        pointer = pointer.next
      else:
        raise IndexError("list index out of range")
    if pointer:
      return pointer.data
    else:
      raise IndexError("list index out of range")

  def __setitem__(self, index, elem):
    # como estamos fazendo a sobrecarga de operador, podemos usar a notação a seguir agora:lista[5] = 9
    pointer = self.head
    for i in range(index):
      if pointer:
        pointer = pointer.next
      else:
        raise IndexError("list index out of range")
    if pointer:
      pointer.data = elem
    raise IndexError("list index out of range")

  def index(self, elem):
    """Retorna o índice do elemento na lista"""
    pointer = self.head
    i = 0
    while(pointer):
      if pointer.data == elem:
        return i
      pointer = pointer.next
      i =+ 1
    raise ValueError("{} is not in list".format(elem))


list = LinkedList()