A, B = map(int, input().split(' '))
C = int(input())
time = A * 60 + B
time = time + C

a = time // 60
b = time % 60

if a > 23 :
  a -= 24

print(a, b)