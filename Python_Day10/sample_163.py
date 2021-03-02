#url에서 호스트 도메인 추출
#문자열 객체의 split() 사용
url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=056&aid=0010999152'

tmp = url.split('/') #'/'로 구분한 결과값들을 tmp 리스트로 저장
domain = tmp[2]
print(domain)