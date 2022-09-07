def numberToWords(num):
    num_to_English = {0: 'Zero', 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
                      8: "Eight", 9: "Nine", 10: 'Ten', 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
                      15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty",
                      30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}

    rlt = []
    if num == 0:
        return "Zero"
    cnt = 1
    while num > 0:
        temp = num % 1000
        digits = temp % 10
        decades = temp // 10 % 10
        hundreds = temp // 100
        two_ = temp % 100
        temp_rlt = ""
        if hundreds > 0:
            temp_rlt += num_to_English[hundreds] + " " + "Hundred"
        if decades > 0:
            if two_ > 0 and two_ <= 19:
                if temp_rlt:
                    temp_rlt += " "
                temp_rlt += num_to_English[two_]
            elif two_ > 19:
                if temp_rlt:
                    temp_rlt += " "
                temp_rlt += num_to_English[decades * 10]
                if digits > 0:
                    temp_rlt += " " + num_to_English[digits]
        else:
            if digits > 0:
                if temp_rlt:
                    temp_rlt += " "
                temp_rlt += num_to_English[digits]

        if temp_rlt:
            if cnt == 2:
                temp_rlt += " " + "Thousand"
            elif cnt == 3:
                temp_rlt += " " + "Million"
            elif cnt == 4:
                temp_rlt += " " + "Billion"
            rlt.append(temp_rlt)
        cnt += 1
        num //= 1000
    rlt.reverse()
    result = ""
    for i in rlt[:-1]:
        result += i + " "
    result += rlt[-1]
    # print(result)
    return result
