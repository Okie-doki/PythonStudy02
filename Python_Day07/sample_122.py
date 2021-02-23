# all() 리스트이 모든 요소가 참인 경우 True, 거짓이 하나라도 포함되면 False
# any() 리스트의 모든 요소가 거짓인 경우에만 False, 참이 하나라도 존재하면 True
listdata1 = [0, 1, 2, 3, 4]
listdata2 = [True, True, True]
listdata3 = ['', [], (), {}, None, False]
print(all(listdata1))
print(any(listdata1))
print(all(listdata2))
print(any(listdata2))
print(all(listdata3))
print(any(listdata3))

'''
거짓으로 판명되는 값
숫자 0
빈 문자열 '', ""
빈 리스트 []
빈 튜플 ()
빈 사전 {}
None
'''