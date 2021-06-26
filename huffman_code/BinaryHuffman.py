class node:
  def __init__(self, character=None, frequency=None, left=None, middle=None, right=None):
    self.character = character
    self.frequency = frequency
    self.left = left
    self.middle = middle
    self.right = right
  
def printBinaryEncoding(tree, encoding=''):
  if tree != None:
    if tree.character != None:
      print('char: {},\tfreq: {},\tencoding: {}'.format(tree.character, tree.frequency, encoding))
    printBinaryEncoding(tree.left,  encoding + '0')
    printBinaryEncoding(tree.right, encoding + '1')

# Extrai o mínimo com custo O(n)
def extractMin(C):
  if C == None:
    return None
  minIndex = 0
  for j in range(0, len(C)):
    if C[j].frequency < C[minIndex].frequency:
      minIndex = j
  return C.pop(minIndex)

def huffman(C):
  Q = C.copy()
  for i in range(0, len(C)-1):
    z = node()
    z.left = x = extractMin(Q)
    z.right = y = extractMin(Q)
    xfreq = x == None if 0 else x.frequency
    yfreq = y == None if 0 else y.frequency
    z.frequency = xfreq + yfreq
    Q.append(z)
  return extractMin(Q)

if __name__ == '__main__':
  C = [node('a', 45), node('b', 13), node('c', 12), node('d', 16), node('e', 9), node('f', 5), node('g', 10)]
  tree = huffman(C)
  printBinaryEncoding(tree)