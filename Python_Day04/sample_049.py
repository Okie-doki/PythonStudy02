class MyClass:
    var = 'hello' #멤버
    def sayhello(self): #메소드
        print(self.var)

obj = MyClass() #MyClass 객체 생성
print(obj.var)
obj.sayhello()