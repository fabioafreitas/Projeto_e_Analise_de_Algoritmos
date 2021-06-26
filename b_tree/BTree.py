import numpy as np

'''
Definition B-Tree
1. Every node has at most m children.
2. Every non-leaf node (except root) has at least ⌈m/2⌉ children nodes.
3. The root has at least two children if it is not a leaf node.
4. A non-leaf node with k children contains k − 1 keys.
5. All leaves appear in the same level and carry no information.


n+1 - Filhos = Ponteiros = Apontam para endereço de outros nodos
n   - Keys = Chaves = Armazenam valores

B-Tree trabalha com fator de espanção de T >= 2

nodos folhas não possui filhos/ponteiros

nodos internos de K chaves possui K+1 filhos/ponteiros (c = k+1)

nodos internos tem:
- no mínimo: T-1 chaves/keys e T filhos/ponteiros
- no máximo: 2T-1 chaves/keys e 2T filhos/ponteiros


'''

class BTreeNode:
    def __init__(self, keys=[], children=[], leaf=False):
        self.keys = keys
        self.children = children
        self.leaf = leaf

class BTree:
    def __init__(self, t, root=BTreeNode(leaf=True)):
        self.t = t
        self.root = root
    
    def print_order(self):
        '''
        imprime no console a árvore em ordem
        (relembrar pré-ordem, ordem e pós-ordem)
        '''
        this_level = [self.root]
        while this_level:
            next_level = []
            output = ""
            for node in this_level:
                if node.children:
                    next_level.extend(node.children)
                output += str(node.keys) + " "
            print(output)
            this_level = next_level
    
    def print_order2(self):
        '''
        imprime no console a árvore em ordem
        (relembrar pré-ordem, ordem e pós-ordem)
        '''
        this_level = [self.root]
        while this_level:
            next_level = []
            output = ""
            for node in this_level:
                if node.children:
                    next_level.extend(node.children)
                output += str([chr(i) for i in node.keys]) + " "
            print(output)
            this_level = next_level
            
    def search(self, value, btnode=None): 
        # btnode é do tipo BTreeNode
        # se btnode for null, pegue o objeto BTreeNode da variabel self.root
        if btnode == None:
            btnode = self.root
        i = 0
        while i < len(btnode.keys) and value > btnode.keys[i]:
            i += 1
        if i < len(btnode.keys) and value == btnode.keys[i]:
            return True # achou o valor
        elif btnode.leaf:
            return False # valor não existe
        else: # Disk-Read
            return self.search(value, btnode.children[i])
    
    def insert(self, value):
        '''
        inserir auxiliar. checa se o btnode
        precisa ser dividido antes de adicionar
        o valor value na arvore
        '''
        root = self.root
        if len(root.keys) == (self.t * 2) - 1:
            # crio um novo nó para apontar para a raiz
            self.root = BTreeNode(children=[root])
            self.__split_child(self.root, 0)
            self.__insert_nonfull(self.root, value)
        else:
            self.__insert_nonfull(root, value)
    
    def __split_child(self, btnode, index):
        '''
        separa um btnode cheio e adiciona a key mediana
        na posição index de btnode.keys
        '''
        y = btnode.children[index]
        z = BTreeNode()
        z.leaf = y.leaf
        z.keys = y.keys[self.t:]  # primeiro laço
        if not y.leaf:
            z.children = y.children[self.t:] # segundo laço
        # inserindo ponteiro de z na posição index de btnode.children
        btnode.children = btnode.children[:index+1] + [z] + btnode.children[index+1:]
        # inserindo a key da mediana no node pai
        btnode.keys = btnode.keys[:index+1] + [y.keys[self.t-1]] + btnode.keys[index+1:]
        #corrigindo filhos e chaves do no direito
        y.keys = y.keys[:self.t-1]
        y.children = y.children[:self.t]  
    
    def __insert_nonfull(self, btnode, value):
        '''
        adiciona o valor value na btree que não
        possua seu nodes cheios. Se durante a recursao 
        um btnode estiver cheio, então o método
        chama a função split para separá-lo antes de prosseguir
        '''
        i = len(btnode.keys)-1
        if btnode.leaf:
            while i >= 0 and value < btnode.keys[i]:
                i -= 1
            btnode.keys = btnode.keys[:i+1] + [value] + btnode.keys[i+1:]
        else:
            while i >= 0 and value < btnode.keys[i]:
                i -= 1
            i += 1
            #Disk-Read(btnode.children[i], value)
            if len(btnode.children[i].keys) == (self.t * 2) - 1:
                self.__split_child(btnode, i)
                if value > btnode.keys[i]:
                    i += 1
            self.__insert_nonfull(btnode.children[i], value)
    
    # Delete a node
    def delete(self, k, x = None):
        if x == None:
            x = self.root
        t = self.t
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
        if x.leaf:
            if i < len(x.keys) and x.keys[i] == k:
                x.keys.pop(i)
                return
            return

        if i < len(x.keys) and x.keys[i] == k:
            return self.delete_internal_node(x, k, i)
        elif len(x.children[i].keys) >= t:
            self.delete(k, x.children[i])
        else:
            if i != 0 and i + 2 < len(x.children):
                if len(x.children[i - 1].keys) >= t:
                    self.delete_sibling(x, i, i - 1)
                elif len(x.children[i + 1].keys) >= t:
                    self.delete_sibling(x, i, i + 1)
                else:
                    self.delete_merge(x, i, i + 1)
            elif i == 0:
                if len(x.children[i + 1].keys) >= t:
                    self.delete_sibling(x, i, i + 1)
                else:
                    self.delete_merge(x, i, i + 1)
            elif i + 1 == len(x.children):
                if len(x.children[i - 1].keys) >= t:
                    self.delete_sibling(x, i, i - 1)
                else:
                    self.delete_merge(x, i, i - 1)
            self.delete(k, x.children[i])

    # Delete internal node
    def delete_internal_node(self, x, k, i):
        t = self.t
        if x.leaf:
            if x.keys[i] == k:
                x.keys.pop(i)
                return
            return

        if len(x.children[i].keys) >= t:
            x.keys[i] = self.delete_predecessor(x.children[i])
            return
        elif len(x.children[i + 1].keys) >= t:
            x.keys[i] = self.delete_successor(x.children[i + 1])
            return
        else:
            self.delete_merge(x, i, i + 1)
            self.delete_internal_node(x.children[i], k, self.t - 1)

    # Delete the predecessor
    def delete_predecessor(self, x):
        if x.leaf:
            return x.keys.pop()
        n = len(x.keys) - 1
        if len(x.children[n].keys) >= self.t:
            self.delete_sibling(x, n + 1, n)
        else:
            self.delete_merge(x, n, n + 1)
        self.delete_predecessor(x.children[n])

    # Delete the successor
    def delete_successor(self, x):
        if x.leaf:
            return x.keys.pop(0)
        if len(x.children[1].keys) >= self.t:
            self.delete_sibling(x, 0, 1)
        else:
            self.delete_merge(x, 0, 1)
        self.delete_successor(x.children)

    # Delete resolution
    def delete_merge(self, x, i, j):
        cnode = x.children[i]

        if j > i:
            rsnode = x.children[j]
            cnode.keys.append(x.keys[i])
            for k in range(len(rsnode.keys)):
                cnode.keys.append(rsnode.keys[k])
                if len(rsnode.children) > 0:
                    cnode.children.append(rsnode.children[k])
            if len(rsnode.children) > 0:
                cnode.children.append(rsnode.children.pop())
            new = cnode
            x.keys.pop(i)
            x.children.pop(j)
        else:
            lsnode = x.children[j]
            lsnode.keys.append(x.keys[j])
            for i in range(len(cnode.keys)):
                lsnode.keys.append(cnode.keys[i])
                if len(lsnode.children) > 0:
                    lsnode.children.append(cnode.children[i])
            if len(lsnode.children) > 0:
                lsnode.children.append(cnode.children.pop())
            new = lsnode
            x.keys.pop(j)
            x.children.pop(i)

        if x == self.root and len(x.keys) == 0:
            self.root = new

    # Delete the sibling
    def delete_sibling(self, x, i, j):
        cnode = x.children[i]
        if i < j:
            rsnode = x.children[j]
            cnode.keys.append(x.keys[i])
            x.keys[i] = rsnode.keys
            if len(rsnode.children) > 0:
                cnode.children.append(rsnode.children)
                rsnode.children.pop(0)
            rsnode.keys.pop(0)
        else:
            lsnode = x.children[j]
            cnode.keys.insert(0, x.keys[i - 1])
            x.keys[i - 1] = lsnode.keys.pop()
            if len(lsnode.children) > 0:
                cnode.children.insert(0, lsnode.children.pop())
    
if __name__ == '__main__':
    b = BTree(
        t=3,
        root=BTreeNode(
            keys=[ord('p')],
            children=[
                BTreeNode(
                    keys=[ord('c'),ord('g'),ord('m')],
                    children=[
                        BTreeNode(
                            leaf=True,
                            keys=[ord('a'),ord('b')]
                        ),
                        BTreeNode(
                            leaf=True,
                            keys=[ord('d'),ord('e'),ord('f')]
                        ),
                        BTreeNode(
                            leaf=True,
                            keys=[ord('j'),ord('k'),ord('l')]
                        ),
                        BTreeNode(
                            leaf=True,
                            keys=[ord('n'),ord('o')]
                        )
                    ]
                ),
                BTreeNode(
                    keys=[ord('t'),ord('x')],
                    children=[
                        BTreeNode(
                            leaf=True,
                            keys=[ord('q'),ord('r'),ord('s')]
                        ),
                        BTreeNode(
                            leaf=True,
                            keys=[ord('u'),ord('v')]
                        ),
                        BTreeNode(
                            leaf=True,
                            keys=[ord('y'),ord('z')]
                        )
                    ]
                )
            ]
        )
    )
    
    a = BTree(t=2)
    letters = ['F', 'S', 'Q', 'K', 'C', 'L', 'H', 'T', 'V', 'W', 'M', 'R', 'N', 'O', 'A', 'B', 'X', 'Y', 'D', 'Z', 'E']
    for i in letters:
        a.print_order2()
        print('\n')
        a.insert(ord(i))