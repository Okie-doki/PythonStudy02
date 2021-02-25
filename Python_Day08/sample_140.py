# write() 인자로 입력된 데이터를 파일에 기록
text = input('파일에 저장할 내용 입력 : ')
f = open('mydata.txt', 'w') #동일한 이름의 파일이 존재할 경우 덮어쓰기
f.write(text)
f.close