# 딕셔너리 values() 메소드는 값만 cncnf
# 딕셔너리 뷰 객체 리턴
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778,
        'Tom':20245, 'Michale':27115, 'Bob':5887,
        'Kelly':7885}
vals = names.values() #사전 뷰 객체 리턴
print(type(vals))
print(vals)

vals_list = list(vals)
ret = sum(vals_list)
print('출생아 수 통계 : %d' %ret)