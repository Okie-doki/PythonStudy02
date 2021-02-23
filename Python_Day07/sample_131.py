# sorted() 사전을 정렬
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778,
        'Tom':20245, 'Michale':27115, 'Bob':5887,
        'Kelly':7885}
ret1 = sorted(names) #사전의 키값을 오름차순으로 정렬
print(ret1) #키값만 출력

def f1(x):
    return x[0]

def f2(x):
    return x[1]

# sorted() key인자를 이용하여 정렬할 기준이 되는 값 지정
# key 인자로 지정되는 값은 반드시 함수
ret2 = sorted(names.items(), key=f1) #f1인 name 기준으로 정렬
print(ret2)

ret3 = sorted(names.items(), key=f2) #f2인 출생아 숫자 기준으로 정렬
print(ret3)

ret4 = sorted(names.items(), key=f2, reverse=True)
print(ret4)