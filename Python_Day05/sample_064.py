h1 = hex(97) # 16진수 변환 0x61, 문자열 리턴
h2 = hex(98) # 16진수 변환 0x62, 문자열 리턴
ret1 = h1 + h2
print(ret1)

#16진수를 10진수 변환, int형 리턴
a = int(h1, 16) 
b = int(h2, 16)
ret2 = a + b #10진수 195가 됨
print(ret2)
print(hex(ret2)) #16진수로 출력