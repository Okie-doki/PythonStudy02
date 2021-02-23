# in 키워드를 이용하여 특정 값이 사전의 key값으로 존재확인
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778,
        'Tom':20245, 'Michale':27115, 'Bob':5887,
        'Kelly':7885}
k = input('이름 입력 : ')
if k in names:
    print('이름이 <%s>인 출상아 수는 <%d>명입니다'%(k, names[k]))
else:
    print('자료에 <%s>인 이름이 존재하지 않습니다'%k)