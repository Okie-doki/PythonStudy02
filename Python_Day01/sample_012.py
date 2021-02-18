# 반복 for ~ contunue ~ break
scope = [1, 2, 3, 4, 5]
for x in scope:
    print(x)
    if x < 3:
        continue #다음 반복문 수행
    else:
        break #for반복만 탈출

scope = [1, 2, 3, 4, 5]
for x in scope:
    print(x)
    if x >= 3:
        break