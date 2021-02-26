import os

newfolder = input('새로 생성할 디렉터리 이름 : ') # 경로를 포함한 디렉터리 이름 (경로가 없으면 해당 위치)
try:
    os.mkdir(newfolder)
    print('[%s] 디렉터리 새로 생성했습니다'%newfolder)
except Exception as e:
    print(e)