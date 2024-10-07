from random import random
N=int(input())
A = [int(random()*10000) for i in range(N)]
for i in range(N):
    for j in range(i,N):
        if A[i] > A[j]:
           z = A[i]
           A[i] = A[j]
           A[j] = z
print(A) 
