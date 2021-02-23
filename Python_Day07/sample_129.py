# items() 모든 요소를 추출하여 사전 뷰 객체러 리턴
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778,
        'Tom':20245, 'Michale':27115, 'Bob':5887,
        'Kelly':7885}
items = names.items()
print(type(items))
print(items)

for item in items:
    print(type(item), item)