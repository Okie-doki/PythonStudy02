# dict1 = {key : value} 딕셔너리 선언
# 리스트와 다르게 순서 없음
dict1 = {'a':1, 'b':2, 'c':3}
print(dict1['a'])
dict1['d'] = 4 # 동일한 key가 없으므로 추가
print(dict1)
dict1['b'] = 7 # 동일한 key가 있으므로 수정
print(dict1)
print(len(dict1))