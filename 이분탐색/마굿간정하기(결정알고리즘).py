def Count(len):
    count = 1
    ep = line[0]
    for i in range(1, n):
        if line[i] - ep >= len:
            count += 1
            ep = line[i]
    return count


n, c = map(int, input().split())
line = []

for _ in range(n):
    a = int(input())
    line.append(a)

line.sort()

lt = line[0]
rt = line[n-1]

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
