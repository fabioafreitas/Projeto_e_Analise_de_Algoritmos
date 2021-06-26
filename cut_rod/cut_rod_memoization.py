import numpy as np

def memo_cut_rod(p,n,r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(1,n+1):
            q = max(q, p[i] + memo_cut_rod(p,n-i,r))
    r[n] = q
    return q

if __name__ == '__main__':
    #nesta implementação, precisamos garantir que a lista de precos tenha 0 na posiçao 0 do array
    prices = [0,5,6,2,4,5,6,2,4]
    memoization = np.full(len(prices),float('-inf'))
    rod_length = 7
    print("solucao otima:")
    print(memo_cut_rod(prices, rod_length, memoization))