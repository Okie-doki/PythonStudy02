# bin() 10진수를 2진수로 변환한 값을 문자열로 리턴
b1 = bin(97)
b2 = bin(98)
ret1 = b1+b2
print(ret1)

a = int(b1, 2) # 10진수 변환
b = int(b2, 2)
ret2 = a + b
print(bin(ret2))