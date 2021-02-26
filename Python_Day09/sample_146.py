# os.path 모듈의 getsize() 사용하여 파일 크기 구하기
from os.path import getsize

file1 = 'stockcode.txt'
file2 = 'img_sample.jpg'
file_size1 = getsize(file1) # 인자로 입력된 파일의 크기를 바이트 크기로 리턴
file_size2 = getsize(file2)

print('File name : %s \tFile Size : %d' %(file1, file_size1))
print('File name : %s \tFile Size : %d' %(file2, file_size2))