# 슬라이싱을 이요하여 지정한 구간의 문자열 출력
txt1 = 'A tale that was not right'
txt2 = '이 또한 지나가리라'
print(txt1[3:7])
print(txt1[:-6])
print(txt2[-4:])

txt = 'python'
for i in range(len(txt)):
    print(txt[:i+1])