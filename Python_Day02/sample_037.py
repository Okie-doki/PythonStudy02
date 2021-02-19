# tuple = () <- 튜플 선언. 요소 변경 불가
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 'a', 'abc', [1, 2, 3, 4, 5], ['a', 'b', 'c'])

print(tuple1)
print(tuple2)
print(tuple3)

# tuple1[0] = 6 요소 변경 불가

def myfunc():
    print('hello')

tuple4 = (1, 2, myfunc)
tuple4[2]()