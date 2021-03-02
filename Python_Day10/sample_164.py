#url에서 쿼리 문자열 추출
#url에서 '?' 뒤에 표시되는 문자열이 쿼리 문자열
#쿼리 문자열은 변수=값으로 '&'로 구분
url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=056&aid=0010999152'

tmp = url.split('?')
queries = tmp[1].split('&')
for query in queries:
    print(query)