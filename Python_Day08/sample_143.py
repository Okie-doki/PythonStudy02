# 바이너리 파일 복사
# 용량이 큰 경우가 많기 때문에 부분을 읽어 복사할 파일에 사용
bufsize = 1024 #메모리 용량 설정
f = open('img_sample.jpg', 'rb')
h = open('img_sample_copy.jpg', 'wb')

data = f.read(bufsize) #용량만큼 읽기
while data:
    h.write(data)
    data = f.read(bufsize)

f.close()
h.close()