N = int(input()) # 4의 배수
if N >=4 :
  if N%4 == 0 :
    n = N//4
    print('long ' * n+'int')