# 함수는 1개 이상의 값을 리턴하거나 리턴값이 없을 수도 있다
# 2개 이상 값을 리턴할 경우 튜플로 전달
def reverse(x, y, z):
    return z, y, x

ret = reverse(1, 2, 3)
print(ret)

r1, r2, r3 = reverse('a', 'b', 'c')
print(r1, r2, r3);