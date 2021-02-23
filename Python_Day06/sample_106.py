# reversed() 인자로 입력된 리스트의 요소 순서를 
# 역순으로 만들어 리턴
listdata = list(range(5))
ret1 = reversed(listdata)
print('원본 리스트', end='')
print(listdata)
print('역순 리스트', end='')
print(list(ret1))

# 슬라이싱을 이용하여 리스트의 요소 역순으로 만듬
ret2 = listdata[::-1]
print('슬라이싱 이용', end='')
print(ret2)