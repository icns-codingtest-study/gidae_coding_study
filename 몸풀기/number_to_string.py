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
n = int(input())
under20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
           "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
upper10 = ["", "Ten", "Twenty", "Thirty", "Forty",
           "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
upper1000 = ["", "Thousand", "Million", "Billion"]

# 10억, 100만, 천, 백


def calculate(integer):

    num_to_English = {0: 'Zero', 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
                      8: "Eight", 9: "Nine", 10: 'Ten', 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
                      15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty",
                      30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
    if integer == 0:
        return "Zero"
