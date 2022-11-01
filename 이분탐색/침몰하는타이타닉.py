# 유럽에서 가장 유명했던 유람선 타이타닉이 침몰하고 있습니다. 유람선에는 N명의 승객이 타고
# 있습니다. 구명보트를 타고 탈출해야 하는데 타이타닉에 있는 구명보트는 2명 이하로만 탈 수 있
# 으며, 보트 한 개에 탈 수 있는 총 무게도 M kg 이하로 제한되어 있습니다.
# N명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소개수를 출력하는
# 프로그램을 작성하세요.
# 5 140
# 90 50 70 100 60
from collections import deque

n, limit = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
p = deque(p)
count = 0
# 한명씩 빼기
while p:
    if len(p) == 1:
        count += 1
        break
    if p[0]+p[-1] > limit:
        # 가장 무거운 사람 pop
        p.pop()
        count += 1

    else:
        p.popleft()
        p.pop()
        count += 1

print(count)
