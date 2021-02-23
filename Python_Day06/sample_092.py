# find() 문자열에서 특정 문자나 문자열이 위치하는 인덱스 리턴
# 인덱스 앞에서부터 최초로 찾는 위치값 리턴
txt = 'A lot of things occur each day, every day'
offset1 = txt.find('e')
offset2 = txt.find('day')
offset3 = txt.find('day', 30) #두번쨰 인자값은 특정 위치 인덱스부터 찾기
print(offset1)
print(offset2)
print(offset3)