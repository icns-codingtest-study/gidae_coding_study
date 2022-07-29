# 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게
# 임이 있다.
# 규칙(1) 같은 눈이 3개가 나오면 10, 000원+(같은 눈)*1, 000원의 상금을 받게 된다.
# 규칙(2) 같은 눈이 2개만 나오는 경우에는 1, 000원+(같은 눈)*100원의 상금을 받게 된다.
# 규칙(3) 모두 다른 눈이 나오는 경우에는(그 중 가장 큰 눈)*100원의 상금을 받게 된다.
n = int(input())

winner = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b == c:
        don = 10000+a*1000
    elif a == b:
        don = 1000+a*100
    elif b == c:
        don = 1000+b*100
    else:
        don = c*100

    if don > winner:
        winner = don
print(winner)
