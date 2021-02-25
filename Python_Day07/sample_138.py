# readline() 텍스트 파일에서 한줄을 읽고 그 내용을 리턴
# 텍스트 용량이 클 경우 read()로 읽을 시 메모리 문제 발생
# readline() 더이상 읽을 내용이 없을 경우 빈 문자열 리턴
f = open('stockcode.txt', 'r')
line_num = 1
line = f.readline()
while line:
    print('%d %s' %(line_num, line), end='') #readline은 줄바꿈 기호가 포함되어 있으므로 end 사용
    line = f.readline()
    line_num += 1
f.close()