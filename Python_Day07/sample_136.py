# 인자를 바꾸어 함수를 반복 호출하여 결과값 얻기(map)
f = lambda x: x*x
args = [1, 2, 3, 4, 5]
ret = map(f, args)
print(list(ret))

#map()은 2개 이상의 반복되는 인자에 대해서도 적용 가능
f1 = lambda x, y: x*x + y
x = [1, 2, 3, 4, 5]
y = [10, 9, 8, 7, 6]
ret1 = map(f1, x, y)
print(list(ret1))