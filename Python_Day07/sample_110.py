# list.insert()는 특정 위치에 새로운 요소 추가
solarsys = ['태양', '수성', '금성', '지구', '화성',
            '목성', '토성', '천왕성', '해왕성']
pos = solarsys.index('목성')
solarsys.insert(pos, '소행성')
print(solarsys)