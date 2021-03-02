#문자열의 각 문자를 그 다음 문자로 바꾸는 코드
#마지막 문자가 제일 처음 문자로 대체
text = input('문장을 입력 : ')
ret = ''
for i in range(len(text)):
    if i != len(text)-1:
        ret += text[i+1]
    else:
        ret += text[0]
print(ret)