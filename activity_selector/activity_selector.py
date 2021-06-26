import numpy as np

def activity_selector(s, f):
  j = 0
  act = [0]
  for i in range(len(f)):
    if s[i] >= f[j]:
      act.append(i)
      j = i
  return act

# Dado um vetor de atividades de tamanho i busco o 
# indice da primeira atividade que se encaixa com a 
# última atividade desse vetor se não houver uma, 
# retorno -1, se sim retoro seu indice
def latest_non_conflict(s, f, i):
  for j in reversed(range(i)):
    if f[j] <= s[i-1]:
      return j
  return -1



def activity_selector_max_profit_aux(s, f, v, n, m):
  # caso base
  if n == 1: 
    return v[n-1]
  # memoization - verifica se subproblema ja foi resolvido
  elif m[n-1] > float('-inf'):
    return m[n-1]
  # caso geral do problema
  else:
    # verificando valor final com o valor da atividade n-1 
    profit1 = v[n-1]
    i = latest_non_conflict(s, f, n)
    if i != -1:
      profit1 = profit1 + activity_selector_max_profit_aux(s, f, v, i+1, m)
    
    # verificando valor final sem o valor da atividade n-1 
    profit2 = activity_selector_max_profit_aux(s, f, v, n-1, m)

    # adiciona maior caso no memoization e o retorna
    m[n-1] = max(profit1, profit2)
    return m[n-1]




def activity_selector_max_profit(start, finish, value):
  num_activities = len(start)
  memoization = np.full(num_activities, float('-inf'))
  memoization[0] = value[0]
  return activity_selector_max_profit_aux(start, finish, value, num_activities, memoization)

def main1():
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

    print('atividades selecionadas (nos íncices do cormen):')
    print([i+1 for i in activity_selector(s,f)])

def main2():
    '''
    Considere uma modificação no problema de seleção de atividades 
    já vistos. Agora, cada atividade $a_i$ tem, em adição ao seu 
    tempo de início e tempo de término, um valor monetário de $v_i$. 
    O objetivo agora não é mais maximizar o número de atividades 
    agendadas, mas sim maximizar o valor monetário das atividades 
    agendadas. Ou seja, deseja-se encontrar um conjunto A de atividades
    compativeis tal que o somatóro abaixo seja maximizado. Dê 
    um algoritmo com custo polinomial no tempo.

    \begin{align*}
    \sum_{a_k \in A}^{}v_k
    \end{align*}
    '''
    # assume-se que as atividades estao ordenadas pelo tempo de finalização
    start =  [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    finish = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    value =  [4, 5, 5, 3, 5, 6, 6, 7, 9, 9, 0]

    print('max: ')
    print(activity_selector_max_profit(start, finish, value))

    
    
if __name__ == '__main__':
    main1()
    print()
    main2() 