1# 45분 일찍 알람 설정하기"
# 원래 설정되어있는 알람을 45분 앞서는 시간으로 바꾸가
H, M = map(int, input().split())

time = H * 60 + M
time -= 45

# 시간이 0보다 작아지면 24시간으로 변형해주는 것
if time < 0:
    time += 24 * 60

h = time // 60
m = time % 60

print(h, m)