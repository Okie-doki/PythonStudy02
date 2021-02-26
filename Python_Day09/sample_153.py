import os

target_folder = 'tmp'
k = input('[%s] 디렉터리를 삭제하시겠습니까? (y/n)' %target_folder) 
if k == 'y':
    try:
        os.rmdir(target_folder) #rmdir 디렉터리 삭제 / tmp 라는 지정된 폴더 삭제
        print('[%s] 디렉터리를 삭제했습니다'%target_folder) 
    except Exception as e:
        print(e)