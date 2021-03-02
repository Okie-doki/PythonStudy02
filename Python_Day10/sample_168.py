#파일에서 특정 단어 개수 계산. find() 사용
def countWord(filename, word):
    with open(filename, 'r') as f:
        text = f.read()
        text = text.lower() #lower() 소문자 변환
        pos = text.find(word) #find() 최초로 나타나는 위치를 저장
        count = 0
        while pos != -1:
            count += 1
            pos = text.find(word, pos+1) #찾은 위치의 다음 위치
    return count

word = input('mydata.txt에서 개수를 구할 단어 입력 : ')
word = word.lower()
ret = countWord('mydata.txt', word)
print('[%s]의 개수 : %d'%(word, ret))