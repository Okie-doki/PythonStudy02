# chr() 코드값에 대응하는 문자 리턴(ord 반대)
val = input('문자 코드값 입력 : ')
val = int(val)
try:
    ch = chr(val)
    print('코드값:%d[%s], 문자:%s'%(val, hex(val), ch))
except ValueError:
    print('입력한 <%d>에 대한 문자가 존재하지 않습니다'%val)