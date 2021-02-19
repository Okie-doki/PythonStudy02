def add_txt(t1, t2='python'): # t2 기본 인자
    print(t1+' : '+t2)

add_txt('best')
add_txt(t2='대한민국', t1='1등') # 키워드 인자

def func1(*args): # 가변인자(가변인자는 * 사용), 튜플로 처리
    print(args)

def func2(width, height, **kwargs): # kwargs 미정 키워드 인자
    print(kwargs)

func1()
func1(3, 5, 1, 5)
func2(10, 20)
func2(10, 20, depth=50, color='blue')