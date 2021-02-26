spos = 105
size = 500

f= open('stockcode.txt', 'r')
h = open('stockcode_part.txt', 'w')

f.seek(spos) # 파일의 특정 부분만 읽기 위해 seek() 이용하여 위치 이동
data = f.read(size)
h.write(data)

h.close()
f.close()