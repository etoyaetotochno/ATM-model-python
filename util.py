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

def check_phone(phone):
    if len(phone) != 10:
        return False
    if not phone.startswith("0"):
        return False
    if not phone.isdigit():
        return False
    return True

def count_banknotes(amount):
    denominations = [1000, 500, 200, 100]
    count_1000 = 0
    count_500 = 0
    count_200 = 0
    count_100 = 0

    for denomination in denominations:
        if amount >= denomination:
            count = amount // denomination
            amount %= denomination
            if denomination == 1000:
                count_1000 = count
            elif denomination == 500:
                count_500 = count
            elif denomination == 200:
                count_200 = count
            elif denomination == 100:
                count_100 = count

    result = f"{count_1000}x1000грн, {count_500}x500грн, {count_200}x200грн, {count_100}x100грн"

    return result