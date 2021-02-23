# key:value 순서가 없는 자료형
# key로 해당 요소의 값에 접근
solar1 = ['태양', '수성', '금성', '지구', '화성',
          '목성', '토성', '천왕성', '해왕성']
solar2 = ['Sun', 'Mercury', 'Venus','Earth', 'Mars', 
        'Jupiter', 'Saturn', 'Uranus', 'Neptune']
soladict = {} #딕셔너리 선언
for i, k in enumerate(solar1):
    val = solar2[i]
    soladict[k] = val
print(soladict)