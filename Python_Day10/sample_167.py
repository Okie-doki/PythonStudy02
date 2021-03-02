#텍스트 파일에서 공백으로 구분된 단어의 개수. split() 사용
with open('mydata.txt', 'r') as f:
    data = f.read()
    tmp = data.split()
    print('단어수 : [%d]'%len(tmp))