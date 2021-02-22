# finally는 무조건 실행
try:
    print('안녕하세요')
    print(param)
except:
    print('예외 발생')
finally:
    print('무조건 실행')