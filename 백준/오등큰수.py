import sys

n = int(sys.stdin.readline())
# tmp = list(map(int, input().split()))
tmp = list(map(int, sys.stdin.readline().split()))
dap = []
for i in range(len(tmp)):
    count = 0
    for j in range(i+1, len(tmp)):
        if tmp[i] > tmp[j]:
            count += 1  
    dap.append(count)

for i in range(len(dap)):
    if dap[i] == 0:
        print(-1, end=" ")
    else:
        print(dap[i], end=" ")
