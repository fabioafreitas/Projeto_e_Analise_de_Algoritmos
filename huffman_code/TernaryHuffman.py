class node:
  def __init__(self, character=None, frequency=None, left=None, middle=None, right=None):
    self.character = character
    self.frequency = frequency
    self.left = left
    self.middle = middle
    self.right = right

# Extrai o mínimo com custo O(n)
def extractMin(C):
  if C == None:
    return None
  minIndex = 0
  for j in range(0, len(C)):
    if C[j].frequency < C[minIndex].frequency:
      minIndex = j
  return C.pop(minIndex)

def printTernaryEncoding(tree, encoding=''):
  if tree != None:
    if tree.character != None:
      print('char: {},\tfreq: {},\tencoding: {}'.format(tree.character, tree.frequency, encoding))
    printTernaryEncoding(tree.left,   encoding + '0')
    printTernaryEncoding(tree.middle, encoding + '1')
    printTernaryEncoding(tree.right,  encoding + '2')
    

def huffmanTernary(C):
  Q = C.copy()
  for i in range(0, len(C)-1):
    if len(Q) == 1:
        break
    z = node()
    z.left = l = extractMin(Q)
    z.middle = m = extractMin(Q)
    z.right = r = extractMin(Q)
    lfreq = mfreq = rfreq = 0
    if l != None:
        lfreq = l.frequency
    if m != None:
        mfreq = m.frequency
    if r != None:
        rfreq = r.frequency
    z.frequency = lfreq + mfreq + rfreq
    Q.append(z)
  return extractMin(Q)

if __name__ == '__main__':
    C = [node('a', 45), node('b', 13), node('c', 12), node('d', 16), node('e', 9), node('f', 5), node('g', 10)]
    tree = huffmanTernary(C)
    printTernaryEncoding(tree)