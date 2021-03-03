#url 접속하여 html 페이지 출력
#urlopen() 이용하여 html 소스 코드를 출력
from urllib.request import urlopen

url = 'https://www.python.org'
with urlopen(url) as f:
    doc = f.read().decode()
    print(doc)