# ord() 문자 하나에 대응하는 코드값 정수형으로 리턴
ch = input('문자 1개 입력 : ')
if len(ch) != 0:
    ch = ch[0]
    chv = ord(ch)
    print('문자 : %s \t코드값 : %d[%s]'%(ch, chv, hex(chv)))