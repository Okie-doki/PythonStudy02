#파일에서 특정 문자열 교체. replace()사용
t1 = input('찾을 단어 입력 : ')
t2 = input('변경할 단어 : ')

with open('mydata.txt', 'r') as f: #읽기모드
    with open('mydata2.txt', 'w') as h: #쓰기모드
        text = f.read()
        text = text.replace(t1, t2) #replace(t1, t2) t1단어를 t2단어로 변경
        h.write(text)
    
print('[%s]를 [%s]로 변경'%(t1, t2))