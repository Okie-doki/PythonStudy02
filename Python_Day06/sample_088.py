# 문자열에서 공백 제거
txt = ' 양쪽에 공백이 있는 문자열입니다 '
ret1 = txt.lstrip() # 왼쪽 공백 제거
ret2 = txt.rstrip() # 오른쪽 공백 제거
ret3 = txt.strip() # 좌우 공백 제거
print('<'+txt+'>')
print('<'+ret1+'>')
print('<'+ret2+'>')
print('<'+ret3+'>')