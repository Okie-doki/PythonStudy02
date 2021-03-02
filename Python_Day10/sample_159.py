from time import localtime

weekdays = ['월요일', '화요일', '수요일', '목요일',
            '금요일', '툐요일', '일요일']
t = localtime()
today = '%d-%d-%d'%(t.tm_year, t.tm_mon, t.tm_mday)
week = weekdays[t.tm_wday] #월요일=0, 화요일=1 ~ 일요일=6

print('[%s] 오늘은 [%s]입니다'%(today, week))