# random 모듈의 shuffle()은 리스트 요소를 무작위로 섞음
from random import shuffle

listdata = list(range(1, 11))
for i in range(3):
    shuffle(listdata)
    print(listdata)