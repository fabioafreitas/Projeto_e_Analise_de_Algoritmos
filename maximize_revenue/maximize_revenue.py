'''
# 3º)

Suponha que lhe são dados dois conjuntos $A$ e $B$, cada qual contendo 
$n$ inteiros positivos. Você pode escolher reordenar os conjuntos de 
qualquer forma. Após o reordenamento, seja $a_i$ o i-ésimo elemento 
do conjunto $A$, e seja $b_i$ o i-ésimo elemento do conjunto $B$. 
Você irá receber um pagamento dado ela produtório abaixo. Dê um 
algorimto que maximiza o seu pagamento e mostre qual é o seu
custo em tempo.

\begin{align*}
\prod_{i=1}^{n}a_i^{b_i}
\end{align*}


# 3º)

Suponha que lhe são dados dois conjuntos $A$ e $B$, cada qual
contendo $n$ inteiros positivos. Você pode escolher reordenar 
os conjuntos de qualquer forma. Após o reordenamento, seja 
$a_i$ o i-ésimo elemento do conjunto $A$, e seja $b_i$ o i-ésimo
elemento do conjunto $B$. Você irá receber um pagamento dado ela
produtório abaixo. Dê um algorimto que maximiza o seu pagamento 
e mostre qual é o seu custo em tempo.

\begin{align*}
\prod_{i=1}^{n}a_i^{b_i}
\end{align*}
'''

import numpy as np

def calcular_salario(A, B):             
  if 0 in A:                            # n           custo de buscar o 0 num array de tamanho n
    return 0                            # 1           constante
  else:                                 # 1           constante
    A = np.sort(A, kind='mergesort')    # n*log(n)    custo do mergesort é n*log(n)
    B = np.sort(B, kind='mergesort')    # n*log(n)    custo do mergesort é n*log(n)
    total = 1                           # 1           constante           
    for i in range(len(A)):             # n           loop com as n iterações do produtório
      total = total * A[i]**B[i]        # 1           constante
    return total                        # 1           constante

if __name__ == '__main__':
    num = 4
    A = np.random.randint(low=1,high=num+1, size=num) # lista de números aleatorios entre 1 e 4
    B = np.random.randint(low=1,high=num+1, size=num) # lista de números aleatorios entre 1 e 4
    print("A = {}\nB = {}\nTotal = {}".format(A,B,calcular_salario(A,B)))