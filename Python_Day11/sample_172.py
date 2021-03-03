# 인터넷에 있는 이미지를 내 pc 저장
from urllib.request import urlopen

imgurl = 'http://www.infopub.co.kr/l_pic/06000238.jpg'
imgname = imgurl.split('/')[-1] #이미지 이름 추출
try:
    with urlopen(imgurl) as f:
        with open(imgname, 'wb') as h: #바이너리 쓰기모드
            img = f.read()
            h.write(img)
except Exception as e:
    print(e)
