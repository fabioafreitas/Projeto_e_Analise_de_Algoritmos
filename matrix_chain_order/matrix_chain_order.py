import numpy as np

def get_indexes(matrices):
  p = []
  p.append(matrices[0].shape[0])
  for matrix in matrices:
    p.append(matrix.shape[1])
  return p

def matrix_chain_order(p):
  n = len(p) - 1
  m = np.zeros((n+1,n+1))
  s = np.zeros((n+1,n+1))

  for l in range(2,n+1): # l é o offset com relação a diagonal principal
    for i in range( 1 , n - l + 2): #( n - l + 2, o 2 é para corrigir a posição inicial de arrays do python (0) com o do cormen (1))
      j = i + l - 1   # i + l - 1 calcula a celula atual na atual diagonal 
      m[i,j] = float('inf')
      for k in range(i,j):
        q = m[i,k] + m[k+1,j] + p[i-1]*p[k]*p[j]
        if q < m[i,j]:
          m[i,j] = q
          s[i,j] = k
  return m, s

def matrix_chain_multiply(matrices, s, i, j): # s representa a memoização para colocacao dos parenteses
  if i == j:
    return matrices[i-1]
  else:
    m1 = matrix_chain_multiply(matrices, s, i, int(s[i,j]) )
    m2 = matrix_chain_multiply(matrices, s, int(s[i,j]) + 1 , j)
    return np.matmul(m1, m2)

def main1():
    # Exemplo do cormen
    matrices = []
    matrices.append(np.random.randint(2, size=(30,35)))
    matrices.append(np.random.randint(2, size=(35,15)))
    matrices.append(np.random.randint(2, size=(15,5)))
    matrices.append(np.random.randint(2, size=(5,10)))
    matrices.append(np.random.randint(2, size=(10,20)))
    matrices.append(np.random.randint(2, size=(20,25)))

    p = get_indexes(matrices)
    m, s = matrix_chain_order(p)
    print('Número min de multiplicações:')
    print(m)
    print('\nColocação dos parênteses:')
    print(s)
    
def main2():
    # Exemplo do slide
    matrices = []
    matrices.append(np.random.randint(2, size=(10,100)))
    matrices.append(np.random.randint(2, size=(100,5)))
    matrices.append(np.random.randint(2, size=(5,50)))

    p = get_indexes(matrices)
    m, s = matrix_chain_order(p)
    print('Número min de multiplicações:')
    print(m)
    print('\nColocação dos parênteses:')
    print(s)
    
    n = len(p) - 1
    r = matrix_chain_multiply(matrices, s, 1, n)

    print('dimensões da matrix resultante:')
    print(r.shape)

if __name__ == '__main__':
    main2()