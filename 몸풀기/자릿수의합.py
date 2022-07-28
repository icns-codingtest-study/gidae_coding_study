# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
# 하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를
# 꼭 작성해서 프로그래밍 하세요.

n = int(input())
a = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum


max = 0
for i in a:
    tot = digit_sum(i)
    if tot > max:
        max = tot
        dap = i
print(i)
