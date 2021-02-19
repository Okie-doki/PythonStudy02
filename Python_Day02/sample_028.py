# 슬라이싱 [시작 인덱스 : 끝 인덱스 : 스탭(간격)]
strdata = 'time is money'
print(strdata[1:5]) # 인덱스 1번에서 4번까지 값
print(strdata[:7]) # 인덱스 0번부터 6번까지 값
print(strdata[9:]) # 인덱스 9번부터 끝까지
print(strdata[:-3])
print(strdata[:]) # 모든 인덱스 출력
print(strdata[::2]) # 모든 인덱스 중 홀수