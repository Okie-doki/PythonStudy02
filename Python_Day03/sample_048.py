# 파일을 열기 위해 open 함수 사용
# open(파일이름, 모드), r은 텍스트 모드로 읽기
f = open('text.txt', 'r')

# 파일 처리 코드 작성

# open() 함수를 사용했으면 close() 함수 필수
f.close()