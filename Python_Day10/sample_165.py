#스택 구현. 스택은 나중에 저장된 것이 먼저 추출
mystack = []

def putdate(data): #저장
    global mystack
    mystack.append(data)

def popdata(): #데이터 추출
    global mystack
    if len(mystack) == 0:
        return None
    return mystack.pop()

putdate('데이터1')
putdate([3, 4, 5, 6])
putdate(12345)

print('<스택상태> : ', end='')
print(mystack)

ret = popdata()
while ret != None:
    print('스택에서 데이터 추출 : ', end='')
    print(ret)
    print('<스택상태> : ', end='')
    print(mystack)
    ret = popdata()