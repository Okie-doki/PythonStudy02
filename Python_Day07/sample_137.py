# read() 텍스트 파일 읽고 출력 하기
f = open('stockcode.txt', 'r') #'r' 텍스트 읽기 모드
data = f.read() # read() 모든 내용을 한번에 읽어서 담음
print(data)
f.close()