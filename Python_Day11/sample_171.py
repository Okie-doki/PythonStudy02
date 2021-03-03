#url 이용하여 해당 웹페이지를 html 파일 저장
from urllib.request import urlopen

url = 'http://www.python.org/'

#방법 1 read() 바이트 스트림으로 읽어 decode() 텍스트로 변환
with urlopen(url) as f:
    doc = f.read().decode() #해당 리소스를 바이트 스트림으로 읽어 유니코드 변환
    #교재와 동일하게 open()하면 오류 발생
    #write하려는 데이터와 write target 파일의 인코딩 형식이 맞지 않아 발생
    #open() 인자에 -1, 'utf-8' 버퍼옵션과 인코딩을 지정하여 해결
    with open('pythonhome.html', 'w', -1, 'utf-8') as h:
        h.writelines(doc)

#방법 2 바이트 스트림을 유니코드로 디코딩하지 않고 바이너리 쓰기 모드로 오프닝하여 바이트 스트림 저장
with urlopen(url) as f:
    doc = f.read()
    with open('pythonhome1.html', 'wb') as h:
        h.write(doc)