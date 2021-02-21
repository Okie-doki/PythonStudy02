# 상속해 주는 클래스 = 부모클래스, 슈퍼클래스
# 상속받는 클래스 = 자식클래스, 서브클래스
class Add: #부모 클래스
    def add(self, n1, n2):
        return n1 + n2

class Calculator(Add): # Add 클래스를 상속 받은 자식 클래스
    def sub(self, n1, n2):
        return n1 - n2

obj = Calculator()
print(obj.add(1, 2))
print(obj.sub(1, 2))
