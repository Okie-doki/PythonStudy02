import time # 내장 모듈
import sample_043_import02 # 개인이 작성한 모듈
import mypackage.sample_043_import # mypackage에 있는 모듈

time.sleep(1)
ret1 = sample_043_import02.add_txt('나는', '파이썬이다')
ret2 = mypackage.sample_043_import.reverse(1, 2, 3)
print(ret1)
print(ret2)