import numpy as np

def print_memoization_lcs(X,Y,matrix):
  print('\t\t',end='')
  print(*Y,sep='\t')
  for i in range(matrix.shape[0]):
    if i > 0: 
      print(X[i-1],end='')
    print('\t',end='')
    print(*matrix[i], sep='\t')
    
def print_lcs_aux(X,b,i,j):
  if i == 0 or j == 0:
    return None
  elif b[i,j] == '🡤':
    print_lcs_aux(X,b,i-1,j-1)
    print(X[i-1],end='')
  elif b[i,j] == '🡡':
    print_lcs_aux(X,b,i-1,j)
  else:
    print_lcs_aux(X,b,i,j-1)

def print_lcs(X,Y,b):
  i = len(X)
  j = len(Y)
  print_lcs_aux(X,b,i,j)
  
def lcs_length(X, Y):
  m = len(X)
  n = len(Y)
  b = np.full((m+1,n+1), '0')
  c = np.full((m+1,n+1), 0)
  for i in range(1, m+1):
    for j in range(1, n+1):
      if X[i-1] == Y[j-1]:
        c[i, j] = c[i-1, j-1] + 1
        b[i, j] = '🡤' # diagonal
      elif c[i-1, j] >= c[i, j-1]:
        c[i, j] = c[i-1, j]
        b[i, j] = '🡡' # cima
      else:
        c[i, j] = c[i, j-1]
        b[i, j] = '🡠' # esquerda
  return c, b

def print_lcs_new_aux(X, Y, c, i, j): 
  if c[i, j] == 0:
    return None
  if X[i-1] == Y[j-1]:
    print_lcs_new_aux(X, Y, c, i-1, j-1)
    print(X[i-1],end='')
  elif c[i-1, j] >= c[i, j-1]:
    print_lcs_new_aux(X, Y, c, i-1, j)
  else:
    print_lcs_new_aux(X, Y, c, i, j-1)
  
def print_lcs_new(X,Y,c):
  i = len(X)
  j = len(Y)
  print_lcs_new_aux(X,Y,c,i,j)

def main1():
    x = list('ABCBDAB')    
    y = list('BDCABA')    
    c, b = lcs_length(x, y)

    print('matriz b:')
    print_memoization_lcs(x, y, b)
    print('\nlongest common sequence:')
    print_lcs(x, y, b)

def main2():
    '''
    Dê o pseudo-código para reconstruir uma LCS 
    (sequência comum mais longa possível) a partir de tabela 
    $c$ já computada e as sequências originais 
    $X = <x_1, x_2, ..., x_m>$ e $Y = <y_1, y_2, ..., y_n>$ 
    com um custo de tempo de $O(m+n)$, sem utilizar a tabela $b$.
    '''
    x = list('ABCBDAB')    
    y = list('BDCABA')    
    c, b = lcs_length(x, y)

    print('matriz c:')
    print_memoization_lcs(x, y, c)
    print('\nlongest common sequence:')
    print_lcs_new(x, y, c)
    
if __name__ == '__main__':
    main1()
    print()
    main2()