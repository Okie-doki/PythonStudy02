# 복사할 파일 용량이 크지 않다면 read()를 이용하여 한번에 읽어 write()로 기록
f = open('stockcode.txt', 'r')
h = open('stockcode_copy.txt', 'w')

data = f.read()
h.write(data)

f.close()
h.close()