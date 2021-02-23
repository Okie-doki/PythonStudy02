# str.isalnum() str의 모든 요소가 언어 문자 또는 숫자로만 구성되어 있으면 True
txt1 = '안녕하세요?'
txt2 = '1.Title-제목을 넣으세요'
txt3 = '3피오R2D2'
ret1 = txt1.isalnum() #?가 있어 false
ret2 = txt2.isalnum() #.와 -가 있어 false
ret3 = txt3.isalnum()
print(ret1)
print(ret2)
print(ret3)