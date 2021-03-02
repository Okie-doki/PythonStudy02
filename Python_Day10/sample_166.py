#문장에 나타나는 문자 빈도수
def getTextFreq(filename):
    with open(filename, 'r') as f:
        text = f.read()
        fa = {} #딕셔너리 선언 {문자:빈도수}
        for c in text:
            if c in fa: #문자가 존재하면 +1
                fa[c] += 1
            else: #문자가 존재하지 않으면 1
                fa[c] = 1
    return fa

ret = getTextFreq('mydata.txt')
ret = sorted(ret.items(), key=lambda x:x[1], reverse=True)
for c, freq in ret:
    if c == '\n':
        continue
    print('[%c] -> [%d]회 나타남'%(c, freq))