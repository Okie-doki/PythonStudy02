# lambda 함수는 이름없는 한줄짜리 함수(임시함수)
# lambda 인자, 인자 ... : 실행코드
add = lambda x, y:x+y
ret = add(1, 3)
print(ret)

funcs = [lambda x: x+'.pptx', lambda x: x+'.docx']
ret1 = funcs[0]('Intro')
ret2 = funcs[1]('Report')
print(ret1)
print(ret2)

names = {'Mary':10999, 'Sams':2111, 'Aimy':9778,
        'Tom':20245, 'Michale':27115, 'Bob':5887,
        'Kelly':7885}

ret3 = sorted(names.items(), key=lambda x:x[0])
print(ret3)
