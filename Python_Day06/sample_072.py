# max() min() 최대 최소값 리턴
listdata = [9.96, 1.27, 5.07, 6.45, 8.38,
            9.29, 4.93, 7.73, 3.71, 0.93]
maxval = max(listdata)
minval = min(listdata)
print(maxval) #9.96 출력
print(minval) #0.93 출력

txt = 'Alotofthingsoccureachday'
maxval = max(txt)
minval = min(txt)
print(maxval) #'y' 출력
print(minval) #'A' 출력

maxval = max(2+3, 2*3, 2**3, 3**2)
minval  = min('abz', 'a12')
print(maxval) #9출력
print(minval) #'a12'출력