# 1바이트에서 하위 4비트 추출
# 1바이트는 0x0F와 & 연산을 수행하면 하위 4비트 값만 남음
a = 107 #16진수 0x6b
b = a & 0x0f
print(b) #11출력. 11은 16진수로 b