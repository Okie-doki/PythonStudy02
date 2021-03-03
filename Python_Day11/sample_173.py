#인터넷에 있는 대용량 파일을 내 pc로 저장
from urllib.request import urlopen

BUFSIZE = 256*1024 #대용량 파일을 읽기 위해 메모리 용량(256kb) 지정

fileurl = 'https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe'
filename = fileurl.split('/')[-1]
try:
    with urlopen(fileurl) as f:
        with open(filename, 'wb') as h: #바이너리 쓰기 모드
            buf = f.read(BUFSIZE) #bufsize만큼 읽음
            while buf: #bufsize만큼 읽어서 저장 반복
                h.write(buf)
                buf = f.read(BUFSIZE)
except Exception as e:
    print(e)