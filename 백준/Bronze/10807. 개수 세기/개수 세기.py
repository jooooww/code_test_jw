# 1차원 배열
N = int(input())

A = list(map(int, input().split()))

v = int(input())

for i in range(N):
  if A[i]>= -100 and A[i]<=100:
    pass
if v >= -100 and v <= 100:
      print(A.count(v))