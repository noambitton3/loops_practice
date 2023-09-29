def solution_adv_2():
    print("Please enter a limit to the multiplication table.",
          INPUT_TO_EXIT, "to exit")
    limit = int(input())
    while limit != INPUT_TO_EXIT:
        for i in range(1, limit + 1):
            row = ''
            for j in range(1, limit + 1):
                row += '    ' + str(i * j)
            print(row)
        print("Please enter a limit to the multiplication table.",
              INPUT_TO_EXIT, "to exit")
        limit = int(input())


INPUT_TO_EXIT = -1
solution_adv_2()



