# enumerate() 리스트를 인자로 받아 (인덱스, 요소)쌍인 리스트를 생성
solarsys = ['태양', '수성', '금성', '지구', '화성',
            '목성', '토성', '천왕성', '해왕성']
ret = list(enumerate(solarsys))
print(ret)

for i, body in enumerate(solarsys):
    print('태양계의 %d번째 천체 : %s'%(i, body))