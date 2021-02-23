# 문자열을 int float 강제 형변환
numstr = input('숫자 입력 : ')
try:
    num = int(numstr)
    print('당신이 입력한 숫자는 정수<%d>입니다'%num)
except:
    try:
        num = float(numstr)
        print('당신이 입력한 숫자는 실수<%f>입니다'%num)
    except:
        print('+++숫자를 입력하세요+++')