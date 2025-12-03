a = int(input())
b = list(map(int, input()))

s = 0
sum = []
i = len(b)-1
while i >= 0 :
  s = a * b[i]
  sum.append(s)
  i-=1

three = sum[0]
four = sum[1]
five = sum[2]

six = sum[0] + sum[1]*10 + sum[2] * 100


print(three)
print(four)
print(five)
print(six)