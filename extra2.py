def check_x(boom_num, number):
    if number % boom_num == 0:
        return True
    elif str(boom_num) in str(number):
        return True
    return False


def sort_game(boom_num, range_number):
    all_nums = ''
    for i in range(1, range_number+1):
        if check_x(boom_num, i):
            all_nums += 'boom '
        else:
            all_nums += str(i) + ' '
    return all_nums


def check_input():
    number = int(input('enter a BOOM number: '))
    while number < 1 or number > 9:
        print('number is not in possible range.')
        number = int(input('enter a BOOM number: '))
    return number


boom_number = check_input()
range_num = int(input('enter a range number: '))
print(sort_game(boom_number, range_num))
