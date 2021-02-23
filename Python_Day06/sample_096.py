# 파이썬3 모든 문자열은 유니코드로 처리
# 일부 라이브러리에서는 문자열이 바이트 객체로만 처리되는 경우 존재
# 문자열을 바이트 객체로 바꾸기 encode
u_txt = 'I love python'
b_txt = u_txt.encode() # 문자열을 바이트 객체 바꾸기, UTF-8로 인코딩
print(u_txt)
print(b_txt)

ret1 = 'I' == u_txt[0]
ret2 = 'I' == b_txt[0]
print(ret1)
print(ret2)