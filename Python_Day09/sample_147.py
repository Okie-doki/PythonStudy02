from os import remove

target_file = 'stockcode_copy.txt'
k = input('[%s]파일을 삭제하시겠습니까? (y/n)' %target_file)
if k == 'y':
    remove(target_file) #remove() 삭제하려고 하는 파일의 경로를 인자로 받음
    print('[%s]를 삭제했습니다' %target_file)