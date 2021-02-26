import os

pdir = os.getcwd() # os.getcwd() 현재 디렉터리 위치
print(pdir)

os.chdir('..') # 부모 디렉터리 이동
print(os.getcwd())
os.chdir(pdir) # 이전 작업 디렉터리 이동
print(os.getcwd())