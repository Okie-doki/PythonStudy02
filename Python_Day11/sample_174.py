# 큰 용량 파일을 작은 파일(3MB)들로 분리
filename = 'python-3.9.2-amd64.exe' #173 예제에서 받은 파이썬 설치 파일 사용
subsize = 1024*1024*3 #3MB
suffix = 0

with open(filename, 'rb') as f:
    buf = f.read(subsize) #subsize만큼 데이터 읽음
    while buf:
        subfilename = filename + '_' + str(suffix)
        with open(subfilename, 'wb') as h: #바이너리 쓰기모드로 buf만큼 저장 반복
            h.write(buf)
            print('[%s]완료'%subfilename)
        buf = f.read(subsize)
        suffix += 1