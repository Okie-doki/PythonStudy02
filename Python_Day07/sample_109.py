# list.append() list의 마지막에 요소 추가
listdata = []
for i in range(3):
    txt = input('리스트에 추가할 값을 입력[%d/3] : '%(i+1))
    listdata.append(txt)
    print(listdata)