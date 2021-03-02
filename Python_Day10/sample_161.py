#주어진 숫자를 천 단위로 구분(천 단위마다 콤마)
num = input('아무 숫자 입력 : ')
print(num.isdigit())
if num.isdigit(): #입력받은 문자열이 숫자로만 구성되어 있는지 확인
    num = num[::-1] #숫자를 거꾸로 배열처리
    ret = ''
    for i, c in enumerate(num):
        i += 1
        if i != len(num) and i%3 == 0: #3의 배수마다 콤마 삽입
            ret += (c+',')
        else:
            ret += c
    ret = ret[::-1]
    print(ret)
else:
    print('입력한 내용 [%s] : 숫자가 아닙니다'%num)