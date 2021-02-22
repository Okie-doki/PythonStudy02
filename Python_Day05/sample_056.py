# try~except에서 else 다음에 예외가 발생하지 않았을 떄 실행
try:
    print('안녕하세요')
    # print(param)
except:
    print('예외 발생')
else: # 예외 발생 시 실행되지 않음
    print('예외가 발생하지 않았습니다')