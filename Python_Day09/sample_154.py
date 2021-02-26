import shutil
import os

target_folder = './tmp' #파일 경로 및 폴더 설정
print('[%s] 하위 모든 디렉터리 및 파일들을 삭제합니다' %target_folder)
for file in os.listdir(target_folder):
    print(file)
k = input('[%s]를 삭제하겠습니까?(y/n)'%target_folder)
if k == 'y':
    try:
        shutil.rmtree(target_folder) # shutil.rmtree() 인자로 입력된 경로에 해당하는 디렉터리와 하위 디렉터리 및 파일 모두 삭제
        print('[%s]의 모든 하위 디렉터리와 파일들을 삭제했습니다'%target_folder)
    except Exception as e:
        print(e)