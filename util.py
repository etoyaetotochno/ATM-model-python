def luhn(cc_num):
    cc_num = cc_num[::-1]
    cc_num = [int(x) for x in cc_num]
    doubled_second_digit_list = list()
    digits = list(enumerate(cc_num, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)
    doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
    sum_of_digits = sum(doubled_second_digit_list)
    return sum_of_digits % 10 == 0

def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum

