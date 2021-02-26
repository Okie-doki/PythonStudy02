from os import rename

target_file = 'stockcode.txt'
newname = input('[%s]에 대한 새로운 파일이름 입력 : '%target_file)
rename(target_file, newname) # rename() 파일이름 변경
print('[%s] -> [%s]로 파일이름 변경' %(target_file, newname))