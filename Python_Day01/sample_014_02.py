x = 1
total = 0
while 1: # 1은 True 0은 False (무한반복)
    total += x
    if total > 100000: # while 종료 조건
        print(x)
        print(total)
        break
    x += 1