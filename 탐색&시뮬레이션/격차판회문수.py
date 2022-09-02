# 1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는
# 세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요.
# 회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.

a = [list(map(int, input().split())) for _ in range(7)]
count = 0


for i in range(3):
    for j in range(7):
        if a[j][i] == a[j][i+4] and a[j][i+1] == a[j][i+3]:
            count += 1

        if a[i][j] == a[i+4][j] and a[i+1][j] == a[i+3][j]:
            count += 1

print(count)
# 슬라이딩으로도 가능
# tmp = a[j][i:i+5]
# if tmp == tmp[::-1]:  // 뒤집기(가로만 가능)
#     count += 1
