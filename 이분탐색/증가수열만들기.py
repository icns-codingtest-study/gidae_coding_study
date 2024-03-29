# 1부터 N까지의 모든 자연수로 구성된 길이 N의 수열이 주어집니다.
# 이 수열의 왼쪽 맨 끝 숫자 또는 오른쪽 맨 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가수열
# 을 만듭니다. 이때 수열에서 가져온 숫자(왼쪽 맨 끝 또는 오른쪽 맨 끝)는 그 수열에서 제거됩니
# 다.
# 예를 들어 2 4 5 1 3 이 주어지면 만들 수 있는 가장 긴 증가수열의 길이는 4입니다.
# 맨 처음 왼쪽 끝에서 2를 가져오고, 그 다음 오른쪽 끝에서 3을 가져오고, 왼쪽 끝에서 4,
# 왼쪽 끝에서 5를 가져와 2 3 4 5 증가수열을 만들 수 있습니다.

# 5
# 2 4 5 1 3

# 10
# 3 2 10 1 5 4 7 8 9 6

n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = n-1
last = 0
res = ""
tmp = []
while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))

    if a[rt] > last:
        tmp.append((a[rt], 'R'))

    tmp.sort()
    print(tmp)
    if len(tmp) == 0:
        break
    else:
        res = res+tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()
print(len(res))
print(res)
