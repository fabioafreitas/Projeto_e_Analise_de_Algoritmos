from math import floor

def build_min_heap(A): 
  for i in reversed(range(1, floor((len(A))/2))):
    min_heapfy(A, i)

def min_heapfy(A, i):
  l = 2*i
  r = 2*i+1
  if l <= len(A) and A[l] < A[i]:
    smallest = l
  else: 
    smallest = i
  if l <= len(A) and A[r] < A[smallest]:
    smallest = r
  if smallest != i:
    A[i], A[smallest] = A[smallest], A[i]
    min_heapfy(A, smallest)
    
a = [9,3,2,1,0,0]
build_min_heap(a)
print(*a)