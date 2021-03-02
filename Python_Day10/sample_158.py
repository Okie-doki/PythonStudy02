#localtime() 년, 월, 일 시간, 분, 초 요일 경과날짜 등의 정보를 리턴
from time import localtime

t = localtime() #localtime() 현재 시간을 struct_time형식으로 리턴
start_day = '%d-01-01'%t.tm_year #tm_year 현재 년도
elapsed_day = t.tm_yday #1월 1일부터 현재까지 날짜수

print('오늘은 [%s]이후 [%d]일째 되는 날입니다'%(start_day, elapsed_day))