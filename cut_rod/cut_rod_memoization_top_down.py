import numpy as np

def memoization_cut_rod_cut_cost_top_down_aux(p, n, r, cost, where_to_cut):
    if r[n] > 0:
        return r[n]
    if n == 0:
        q = 0  
    else:
        q = r[n]
        for i in range(1,n+1):
            aux = p[i] + memoization_cut_rod_cut_cost_top_down_aux(p,n-i,r,cost, where_to_cut) - cost
            if q < aux:
                q = aux
                where_to_cut[n] = i # lista da posicao dos cortes
    r[n] = q
    return q

def memoization_cut_rod_cut_cost_top_down(prices, rod_lenght, cut_cost):
    memoization = np.full(len(prices),0)
    where_to_cut = np.full(rod_length + 1, 0)
    return memoization_cut_rod_cut_cost_top_down_aux(prices, rod_length, memoization, cut_cost, where_to_cut), where_to_cut


if __name__ == '__main__':
    prices = [0, 1, 5, 8, 10, 13, 17, 17, 20, 24, 30]
    rod_length = 10
    cut_cost = 3

    revenue, cuts = memoization_cut_rod_cut_cost_top_down(prices, rod_length, cut_cost)
    print('prices: {}\nrod length: {}\ncut cost: {}\nrevenue: {}\ncuts: {}'.format(prices,rod_length,cut_cost,revenue, cuts))