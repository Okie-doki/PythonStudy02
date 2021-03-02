from time import localtime, strftime

logfile = 'test.log'
def writelog(logfile, log):
    #localtime() 대한민국 현재시간을 time.strruct_time 형식의 데이터로 리턴
    #strftime() struct_time 형식의 데이터를 포맷 문자열을 이용해 특정 형식으로 표현
    time_stamp = strftime('%Y-%m-%d %X\t', localtime())
    log = time_stamp + log + '\n'
    
    with open(logfile, 'a') as f:
        f.writelines(log)

writelog(logfile, '첫번째 로깅 문장입니다')