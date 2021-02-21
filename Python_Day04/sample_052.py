class MyClass:
    def __init__(self): #인스턴스 멤버 초기화
        self.var = '안녕하세요'
        print('MyClass 인스턴스 객체가 생성되었습니다')

obj = MyClass() # 객체 생성 시 __init__ 자동 호출
print(obj.var)

class MyClass1:
    def __init__(self, txt): # 초기화 시 인자값을 가질 수 있다
        self.var = txt
        print('생성자 인자로 전달받은 값은 <'+self.var+'>입니다')

obj = MyClass1('철수') # 객체 생성 시 인자값 필요
print(obj.var)