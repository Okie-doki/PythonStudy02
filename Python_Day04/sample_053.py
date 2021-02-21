class MyClass:
    def __del__(self):
        print('MyClass 인스턴스 객체가 메모리에서 제거됩니다')

obj = MyClass() # 객체 생성
del obj # 인스턴스 객체를 메모리에서 제거