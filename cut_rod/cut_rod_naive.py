def cut_rod(p,n):
  if n == 0:
    return 0
  q = float('-inf')
  for i in range(1,n+1):
    q = max(q, p[i] + cut_rod(p,n-i))
  return q

if __name__ == '__main__':
    #nesta implementação, precisamos garantir que a lista de precos tenha 0 na posiçao 0 do array
    prices = [0,5,6,2,4,5,6,2,4]
    rod_length = 7
    print("solucao otima:")
    print(cut_rod(prices, rod_length))