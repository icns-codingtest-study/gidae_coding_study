# Integer to English
# Convert a given integer into an English word. Assume that the maximum input number is 999, 999, 999, 999.
# ex)
#     0 -> ‘Zero’
#     1000 -> ‘One Thousand’
#     234 -> ‘Two Hundred Thirty Four’
#     312 -> ‘Three Hundred Twelve’
#     999999999999 -> ‘Nine Hundred Ninety Nine Billion Nine Hundred Ninety Nine Million Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine’

# 10억, 100만
# 20이하 숫자 + 10 단위 숫자
under20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
           "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
multiple_of_10 = ["", "Ten", "Twenty", "Thirty", "Forty",
                  "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
multiple_of_1000 = ["", "Thousand", "Million", "Billion"]

# 10억, 100만, 천, 백
# 100단위부터는 반복되는 부분이 존재하기에 sub 계산을 하나 만든다.
# "Thousand", "Million", "Billion" 단위로 자르면서 string을 더해가며 한다.
# 1000단위로 잘라서 계산  (n = integer % 1000)


def digit_caluate(n):
    # 나머지가 0이므로 return 빈 값
    if n == 0:
        return ""
    # 나머지가 20미만일 때는 미리 만들어 둔 under20 리스트에 인덱스로 접근
    elif n < 20:
        return under20[n] + " "
    # 나머지가 100미만일 때는 n을 10으로 나눈 몫을 mutiple_of_10 리스트에 인덱스로 접근
    # n을 10으로 나눈 나머지를 다시 재귀로 넣어서 계산
    elif n < 100:
        return multiple_of_10[n//10] + " " + digit_caluate(n % 10)
    # n이 100 이상인 경우
    else:
        # 100으로 나눈 몫으로 인덱스 접근 (oo Hundred) + n을 100으로 나눈 나머지로 재귀
        return under20[n//100] + " Hundred " + digit_caluate(n % 100)


# 메인 계산기
def calculate(integer):
    # zero는 특이 케이스라 정확히 지정해준다.
    if integer == 0:
        return "Zero"
    # 영어로 리턴될 변수 초기화
    dap = ""
    # 1000으로 나눠가면서 미리 지정해둔 1000단위 리스트에 인덱스로 접근
    i = 0
    while integer > 0:
        if integer % 1000 != 0:
            # 1000으로 나눈 나머지를 digit_caluate에 넣어서 반복되는 단위를 영어로 바꾸고, 계속 더해 나간다.
            dap = digit_caluate(integer % 1000) + \
                multiple_of_1000[i] + " " + dap
            i += 1
            integer //= 1000

    return dap


print(calculate(int(input())))
