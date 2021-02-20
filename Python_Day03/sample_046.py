# 계층구조로 되어 있는 모듈은 from ~ import로 사용
# from 모듈이름 import 함수이름
# from 패키지이름 import 모듈이름
from time import sleep
from mypackage import sample_043_import
from mypackage.sample_043_import import reverse

sleep(1)
ret1 = sample_043_import.add_txt('나는','파이썬이다')
ret2 = reverse(1, 2, 3)
print(ret1)
print(ret2)