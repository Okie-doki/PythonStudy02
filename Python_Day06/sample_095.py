# replace() 특정 문자나 문자열을 모두 찾아 다른 문자나 문자열로 변경
txt = 'My password is 1234'
ret1 = txt.replace('1', '0')
ret2 = txt.replace('1', 'python')
print(ret1)
print(ret2)

txt = '매일 많은 일들이 일어납니다'
ret3 = txt.replace('매일', '항상')
ret4 = ret3.replace('일', '사건')
print(ret3)
print(ret4)
