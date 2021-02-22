# 예외 발생 가능성 있는 코드는 try와 except 사용
try:
    print('안녕하세요')
    print(param) # NameError
except:
    print('예외가 발생')