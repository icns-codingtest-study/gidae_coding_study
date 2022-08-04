# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의
# 합 A[i]+A[i+1]+…+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오

# 첫째 줄에 N(1≤N≤10, 000), M(1≤M≤300, 000, 000)이 주어진다. 다음 줄에는 A[1], A[2], …,
# A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30, 000을 넘지 않는 자연수이다.

n, m = map(int, input().split())
a = list(map(int, input().split()))

total = a[0]
count = 0
lt = 0
rt = 1

while True:
    if total < m:
        if rt < n:
            total += a[rt]
            rt += 1
        else:
            break

    elif total == m:
        count += 1
        total -= a[lt]
        lt += 1

    else:
        total -= a[lt]
        lt += 1

print(count)
