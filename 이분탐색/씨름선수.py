# 현수는 씨름 감독입니다. 현수는 씨름 선수를 선발공고를 냈고, N명의 지원자가 지원을 했습
# 니다. 현수는 각 지원자의 키와 몸무게 정보를 알고 있습니다.
# 현수는 씨름 선수 선발 원칙을 다음과 같이 정했습니다.
# “다른 모든 지원자와 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나, 무거운 지원자
# 만 뽑기로 했습니다.”
# 만약 A라는 지원자보다 키도 크고 몸무게도 무거운 지원자가 존재한다면 A지원자는 탈락입니
# 다.

n = int(input())
# 지원자 리스트 초기화
list = []
# 지원자 숫자 초기화
count = 0
# 몸무게 최댓값 초기화
largest = 0
for _ in range(n):
    t, w = map(int, input().split())
    list.append((t, w))
print(list)
# 키순으로 정렬
list.sort(reverse=True)
print(list)
for t, w in list:
    if w > largest:
        largest = w
        count += 1
print(count)
