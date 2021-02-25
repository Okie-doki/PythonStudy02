# writelines() 문자열이나 리스트를 인자로 받고 파일에 한줄씩 기록
count = 1
data = []
print('파일에 내용을 저장하려면 내용을 입력하지 말고 [Enter]를 누르세요')
while True:
    text = input('[%d] 파일에 저장할 내용을 입력 : '%count)
    if text == '':
        break
    data.append(text+'\n')
    count += 1

f = open('mydata.txt', 'w')
f.writelines(data) # list의 경우 writelines() 리스트의 요소를 하나의 문자열로 결합하여 기록
f.close()