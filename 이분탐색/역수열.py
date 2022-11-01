# 1부터 n까지의 수를 한 번씩만 사용하여 이루어진 수열이 있을 때, 1부터 n까지 각각의 수 앞
# 에 놓여 있는 자신보다 큰 수들의 개수를 수열로 표현한 것을 역수열이라 한다.
# 예를 들어 다음과 같은 수열의 경우
# 4 8 6 2 5 1 3 7
# 1앞에 놓인 1보다 큰 수는 4, 8, 6, 2, 5. 이렇게 5개이고,
# 2앞에 놓인 2보다 큰 수는 4, 8, 6. 이렇게 3개,
# 3앞에 놓인 3보다 큰 수는 4, 8, 6, 5 이렇게 4개......
# 따라서 4 8 6 2 5 1 3 7의 역수열은 5 3 4 0 2 1 1 0 이 된다.
# n과 1부터 n까지의 수를 사용하여 이루어진 수열의 역수열이 주어졌을 때, 원래의 수열을 출
# 력하는 프로그램을 작성하세요.

n = int(input())
a = list(map(int, input().split()))  # 역수열 5 3 4 0 2 1 1 0
seq = [0] * n
for i in range(n):
    for j in range(n):
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i+1
            break
        elif seq[j] == 0:
            a[i] -= 1
            print(a[i])

for x in seq:
    print(x, end=' ')
