# 딕셔너리 keys() 메소드는 키값만 출력가능한 
# 딕셔너리 뷰 객체 리턴
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778,
        'Tom':20245, 'Michale':27115, 'Bob':5887,
        'Kelly':7885}
ks = names.keys() #사전 뷰 객체 리턴
# 사전 뷰 객체는 사전의 키나 값 등을 동적으로 보여줌
print(type(ks))
print(ks)

for k in ks:
    print('Key:%s \tValue:%d' %(k, names[k]))