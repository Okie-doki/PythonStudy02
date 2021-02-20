# 지역변수는 함수 내부에서만 유효
# 전역변수는 코드 전반에 걸쳐 유효
param = 10
strdata = '전역변수'

def func1():
    strdata = '지역변수'
    print(strdata)

def func2(param):
    param = 1

def func3():
    global param # 함수 내부에서 바깥의 전역변수 사용하기 위해 global
    param = 50

func1() # 지역변수 출력
print(strdata) # 전역변수 출력
print(param) # 10 출력
func2(param)
print(param) # 10 출력
func3()
print(param) # 50 출력