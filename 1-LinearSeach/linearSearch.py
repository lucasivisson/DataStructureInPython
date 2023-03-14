def search(list, elem):
  """Return o índice elem se ele estiver na lista ou None, caso contrário"""
  for i in range(len(list)):
    if list[i] == elem:
      return i
  return None

strange_list = [8, "5", 32, 0, "python", 11]
element = 32;

index = busca(strange_list, element)
if index is not None:
  print("Index of the element {} is {}".format(elemento, indice))
else:
  print("Element {} are not on list".format(elemento))