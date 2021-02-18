scope = [1, 2, 3]
# for ~ else
# for 반복문이 break에 의 해 중단됨이 없을 시 else 실행
for x in scope:
    print(x)
    break #break 주석 처리시 else 문 실행
else:
    print('perfect')

print('fail')