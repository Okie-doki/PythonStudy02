from os import rename

target_file = 'stockcode.txt'
newpath = input('[%s]를 이동할 디렉터리의 절대 경로 입력 : ' %target_file)

if newpath[-1] == '/':
    newname = newpath + target_file
else:
    newname = newpath + '/' + target_file

try:
    # rename() 경로경로까지 포함되어 있다면 해당 경로에 저장
    # 파일명만 있다면 현재 경로가 기본
    rename(target_file, newname) 
    print('[%s] -> [%s]로 이동되었습니다'%(target_file, newname))
except FileNotFoundError as e:
    print(e)