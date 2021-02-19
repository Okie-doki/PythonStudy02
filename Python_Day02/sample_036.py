# list = [] <- list 선언
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [1, 'a', 'abc',
         [1, 2, 3, 4, 5],
         ['a', 'b', 'c']]

print(list1)
print(list2)
print(list3)

list1[0] = 6
print(list1)

def myfunc():
    print('hello')

list4 = [1, 2, myfunc]
print(list4) # 함수 주소값?
list4[2]()