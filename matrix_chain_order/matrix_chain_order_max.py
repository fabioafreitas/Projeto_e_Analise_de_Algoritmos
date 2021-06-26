'''
5º) Considere uma variação do problema da 
Multiplicação da Sequência de Matrizes, no 
qual é desejado definir a ordem de multiplicação 
entre as matrizes tal que o número de multiplicações 
escalares seja maximizado, ao invés de minimizado. 
Este problema exibe uma substrutura ótima? Comente 
sua resposta

Resposta:

O algorimo matrix-chain-order utiliza possui subestrutura 
ótima para resolver o problema. No processo recursivo do
problema, a subestrutura ótima de um dado subproblema é 
encontrada por meio da busca do arrajo de matrizes que 
retornam o menor custo. De forma semelhante, também podemos 
observar essa sub-estrutura ótima no problema da maximização 
do custo, onde só precisamos buscar o arranjo de maior custo 
para resolver o problema original. A versão modificada do algoritmo 
matrix-chain-order para maximizar o custo pode ser encontrada abaixo.
'''

import numpy as np

def get_indexes(matrices):
  p = []
  p.append(matrices[0].shape[0])
  for matrix in matrices:
    p.append(matrix.shape[1])
  return p

def matrix_chain_order_max(p):
  n = len(p) - 1
  m = np.zeros((n+1,n+1))
  s = np.zeros((n+1,n+1))

  for l in range(2,n+1):
    for i in range( 1 , n - l + 2): # n - l + 2, o 2 é para corrigir a posição inicial de arrays do python (0) com o do cormen (1)
      j = i + l - 1 
      m[i,j] = float('-inf')
      for k in range(i,j):
        q = m[i,k] + m[k+1,j] + p[i-1]*p[k]*p[j]
        if q > m[i,j]:
          m[i,j] = q
          s[i,j] = k
  return m, s

# Exemplo do cormen

matrices = []
matrices.append(np.random.randint(2, size=(10,100)))
matrices.append(np.random.randint(2, size=(100,5)))
matrices.append(np.random.randint(2, size=(5,50)))

p = get_indexes(matrices)
m, s = matrix_chain_order_max(p)
print('Número max de multiplicações:')
print(m)
print('\nColocação dos parênteses:')
print(s)