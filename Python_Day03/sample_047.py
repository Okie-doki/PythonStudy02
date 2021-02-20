# import 모듈명 as 별명
import mypackage as mp
import mypackage.sample_043_import as ms

ret1 = mp.sample_043_import.add_txt('대한민국', '1등')
ret2 = ms.reverse(1, 2, 3)

print(ret1)
print(ret2)