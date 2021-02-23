# filter() 특정 조건을 만족하는 값들만 편리하게 추출
# filter 첫번쨰 인자는 함수, 두번째 인자는 리스트와 같이 반복되는 자료
def getPrime(x): #입력된 인자값이 소수인지 판별
    for i in range(2, x-1):
        if x%i == 0:
            break
    else: #break 되지 않고 모두 실행되었을 때 else 실행
        return x
listdata = [117, 119, 1113, 11113, 11119]
ret = filter(getPrime, listdata)
print(list(ret))