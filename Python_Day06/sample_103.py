# 슬라이싱 = 리스틍에서 특정 구간에 있는 요소 추출
solarsys = ['태양', '수성', '금성', '지구', '화성',
            '목성', '토성', '천왕성', '해왕성']
rock_planets = solarsys[1:4]
gas_planets = solarsys[4:]
print('태양계의 암석형 행성 : ', end='')
print(rock_planets)
print('태양계의 가스형 행성 : ', end='')
print(gas_planets)