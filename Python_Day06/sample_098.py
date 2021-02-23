# sorted() 문자열을 정렬하여 리스트로 리턴
strdata = input('정렬할 문자열 입력 : ')
ret1 = sorted(strdata)
ret2 = sorted(strdata, reverse=True) #reverse
print(ret1)
print(ret2)
ret1 = ''.join(ret1) #리스트형을 문자열로 변환
ret2 = ''.join(ret2)
print('오름차순으로 정렬된 문자열은 <'+ret1+'>입니다')
print('내림차순으로 정렬된 문자열은 <'+ret2+'>입니다')

strdata1 = 'qwertyuiop34195'
ret3 = ''.join(sorted(strdata1))
ret4 = ''.join(sorted(strdata1, reverse=True))
print(ret3)
print(ret4)