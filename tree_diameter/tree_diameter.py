class Node:
  def __init__(self, data):
    self.data = data
    self.left = self.right = None

def treeDiameter(root, height = 0):
  if root is None:
    return 0, 0 # diametro atual e altura da árvore atual

  rdiameter, rheight = treeDiameter(root.right)
  ldiameter, lheight = treeDiameter(root.left)
  height = max(lheight, rheight) + 1
  diameter = max(lheight + rheight + 1, ldiameter, rdiameter)
  return diameter, height

def main1():
    """
              1
            /   \
           2      3
          /  \
         4     5
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(treeDiameter(root)[0])

def main2():
    """
               1
             /   \
            2      3
           /  \
          4    5
         /      \
        6        7
       /          \
      8            9

    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(7)
    root.left.right.right.right = Node(9)
    root.left.left.left = Node(6)
    root.left.left.left.left = Node(8)


    print(treeDiameter(root)[0])
if __name__ == '__main__':
    main1()
    print()
    main2()