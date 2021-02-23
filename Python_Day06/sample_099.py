range1 = range(10) #0부터 9까지 리스트
range2 = range(10, 20) #10부터 19까지 리스트
print(list(range1))
print(list(range2))

ret = 0
for i in range(10):
    ret += (i+1)
print(ret)