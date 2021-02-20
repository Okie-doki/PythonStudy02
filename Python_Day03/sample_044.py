# 패키지는 디렉터리(폴더)로 이해
# 패키지명만 import 시 오류발생(이유는??)
# 결국 패키지 내 파일명까지 import
# import mypackage
import mypackage.sample_043_import 

ret1 = mypackage.sample_043_import.add_txt('대한민국','1등')
ret2 = mypackage.sample_043_import.reverse(1, 2, 3)
print(ret1)
print(ret2)