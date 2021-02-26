import os, glob

folder = '.' # 현재 위치
# listdir() 인자로 입력된 경로에 존재하는 모든 파일과 디렉터리 리스트 리턴
file_list = os.listdir(folder)
print(file_list)
print()

# glob() 인자로 입력된 조건이나 경로에 해당하는 파일들을 리턴
file = '*.txt'
file_list = glob.glob(file)
print(file_list)