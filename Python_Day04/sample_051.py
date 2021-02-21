class MyClass:
    def sayHello(self): # self는 인스턴스 객체를 지시하는 참조자
        print('안녕하세요')
    
    def sayBye(self, name): # 인자가 필요하면 self 다음부터 정의
        print('%s! 다음에 보자' %name)

obj = MyClass()
obj.sayHello()
obj.sayBye('철수')