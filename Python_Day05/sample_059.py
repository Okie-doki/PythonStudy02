import time
count = 1
# 특정 예외가 발생했을 때(예외 명시)만 처리
try:
    while True:
        print(count)
        count += 1
        time.sleep(0.5)
except KeyboardInterrupt: # ctrl+c 입력되는 발생
    print('사용자에 의해 프로그램 중단')