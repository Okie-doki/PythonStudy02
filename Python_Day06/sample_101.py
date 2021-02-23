# list index() 메소드는 인자로 입력되는 값에 해당하는 요소의 인덱스 리턴
# index() 메소드는 최초로 나타나는 위치의 인덱스 리턴
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성',
            '토성', '천왕성', '해왕성', '지구']
planet = '지구'
pos = solarsys.index(planet)
print('%s은(는) 태양계에서 %d번째 위치하고 있습니다'%(planet, pos))
pos = solarsys.index(planet, 5)
print('%s은(는) 태양계에서 %d번째 위치하고 있습니다'%(planet, pos))
