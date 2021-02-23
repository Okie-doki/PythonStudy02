txt = 'abcdefghikj'
ret = txt[::-1] # 스탭 -1로 슬라이싱 (문자열 거꾸로 출력)
print(ret)

ret1 = txt[::-2] # 홀수 거꾸로 출력
print(ret1)

ret2 = txt[-2::-2] # 짝수 거꾸로 출력
print(ret2)