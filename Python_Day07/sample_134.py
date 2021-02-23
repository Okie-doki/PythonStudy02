# eval() 파이썬 코드로 실행 가능한 문자열을
# 인자로 받아 실행
expr1 = '2+3'
expr2 = 'round(3.7)'
ret1 = eval(expr1)
ret2 = eval(expr2)
print('<%s>를 eval()로 실행한 결과 : '%expr1, end='')
print(ret1)
print('<%s>를 eval()로 실행한 결과 : '%expr2, end='')
print(ret2)

#실행 가능한 코드면 함수도 가능
def sayHello():
    print('hello python')
tmp = 'sayHello()'
eval(tmp)