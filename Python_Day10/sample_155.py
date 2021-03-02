# 파일이 존재하는 체크(os.path.exists)
import os
from os.path import exists

dir_name = input('새로 생성할 디렉터리 이름을 입력 : ')
if not exists(dir_name): #exists() 인자에 해당하는 파일이나 디렉터리가 존재하면 True
    os.mkdir(dir_name)
    print('[%s] 디렉터리를 생성했습니다'%dir_name)
else:
    print('[%s]은(는) 이미 존재합니다'%dir_name)