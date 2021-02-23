# str.isalpha() str의 모든 요소가 언어 문자로만 구성 되어있는지 확인
txt1 = 'A'
txt2 = '안녕'
txt3 = 'Warcraft Three'
txt4 = '3PO'
ret1 = txt1.isalpha() # True
ret2 = txt2.isalpha() # True
ret3 = txt3.isalpha() # 공백이 있어서 False
ret4 = txt4.isalpha() # 숫자3 False
print(ret1)
print(ret2)
print(ret3)
print(ret4)