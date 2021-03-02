# datetime 객체는 date 객체와 time 객체에서 제공하는 기능들을 모두 제공
from datetime import datetime

start = datetime.now() #datetime.now() 현재 시간을 1/1000초 수준으로 측정
print('1에서 백만까지 더합니다')
ret = 0
for i in range(1000000):
    ret += i
print('1에서 백만까지 더한 결과 : %d'%ret)
end = datetime.now()
elapsed = end - start
print('총 계산 시간 : ', end='')
print(elapsed)
elapsed_ms = int(elapsed.total_seconds()*1000)
print('총 계산 시간 : %dms'%elapsed_ms)