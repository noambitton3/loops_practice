def if_prime(number):
    for i in range(number):
        if i != 0 and i != 1 and i != number:
            out = number % i
            if out == 0:
                return False
    return True


def check_input():
    number = int(input('enter a number: '))
    while number < 2 or number > 100:
        print('number is not in range.')
        number = int(input('enter a number: '))
    return number


def the_diviners(number):
    sum_nums = 0
    num1_final = 0
    num2_final = 0
    for i in range(number):
        if i != 0 and i != 1 and i != number:
            out = number % i
            if out == 0:
                num1 = i
                num2 = number / i
                amount = num1 + num2
                if amount > sum_nums:
                    sum_nums = amount
                    num1_final = num1
                    num2_final = num2
    return int(num1_final), int(num2_final)


num = check_input()
check = if_prime(num)
if check:
    print("the number is Prime number")
else:
    print("the number is NOT Prime number")
    print(the_diviners(num))
