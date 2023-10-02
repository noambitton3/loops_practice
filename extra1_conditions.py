def if_even(number):
    summery = number % 2
    if summery == 0:
        return True
    return False


def if_divide_in_3(number):
    summery = number % 3
    if summery == 0:
        return True
    return False


def check_both_divide(number):
    if if_even(number) and if_divide_in_3(number):
        print('The number is divisible by both 2 and 3')
    elif if_even(number) and if_divide_in_3(number) is False:
        print('The number is divisible only by 2')
    elif if_even(number) is False and if_divide_in_3(number):
        print('The number is divisible only by 3')
    else:
        print('The number is NOT divisible by both 2 and 3')


num = float(input('enter a number: '))
check_both_divide(num)

