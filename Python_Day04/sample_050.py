# 클래스 멤버는 클래스 메소드 바깥에서 선언
# 인스턴스 멤버는 클래스 메소드 내에서 self와 선언
class MyClass:
    var = '안녕하세요' #클래스 멤버
    def sayHello(self): #클래스 메소드
        param1 = '안녕' #지역변수
        self.param2 = '하이'
        print(param1)
        print(self.var)

obj = MyClass()
print(obj.var)
obj.sayHello()
# obj.param1 #클래스 메소드 내 지역변수라 오류