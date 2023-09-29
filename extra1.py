def check_7(number):
    if number % 7 == 0:
        return True
    elif '7' in str(number):
        return True
    return False


def print_game(number):
    all_nums = ''
    for i in range(1, number+1):
        if check_7(i):
            all_nums += 'boom '
        else:
            all_nums += str(i) + ' '
    return all_nums


num = int(input('enter a number: '))
print(print_game(num))
