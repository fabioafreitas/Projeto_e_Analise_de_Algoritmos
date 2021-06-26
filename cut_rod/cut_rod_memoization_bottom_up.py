import numpy as np

def memoization_cut_rod_cut_cost_bottom_up(p, n, cost):
    r = np.full(n+1, 0)
    where_to_cut = np.full(n + 1, 0)
    r[0] = 0
    for j in range(1, n+1):
        q = r[j]
        for i in range(1, j+1):
            aux = p[i] + r[j - i] - cost
            if q < aux:
                q = aux
                where_to_cut[j] = i
        r[j] = q
    return r, where_to_cut

if __name__ == '__main__':
    prices = [0, 1, 5, 8, 10, 13, 17, 17, 20, 24, 30]
    rod_length = 10
    cut_cost = 3
    revenue, cuts = memoization_cut_rod_cut_cost_bottom_up(prices, rod_length, cut_cost)
    print('prices: {}\nrod length: {}\ncut cost: {}\nrevenue: {}\ncuts: {}'.format(prices,rod_length,cut_cost,revenue, cuts))