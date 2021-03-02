# 파일, 디렉터리 확인(isfile, isdir)
import os

from os.path import exists, isdir, isfile

files = os.listdir()
for file in files:
    if isdir(file): # isdir() 인자로 입력된 경로가 디렉터리면 True
        print('dir : %s' %file)

for file in files:
    if isfile(file): # isfile() 인자로 입력된 경로가 파일이면 True
        print('file : %s' %file)