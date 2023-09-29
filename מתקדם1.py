import random
winner = 0
global_count = 1000000
players = int(input("number of players"))
player = 0

for i in range(players):
    count = 0
    num = random.randint(0, 100)
    player += 1
    guess = int(input("PLAYER " + str(player) + " please enter your guess"))
    count += 1
    while num != guess:
        while guess < num:
            print("too low. try again")
            guess = int(input("PLAYER " + str(player) + " please enter your guess"))
            count += 1
        while guess > num:
            print("too high. try again")
            guess = int(input("PLAYER " + str(player) + " please enter your guess"))
            count += 1
    while num == guess:
        print("YOU WON")
        print("the number of guesses is :", count)
        if count < global_count:
            global_count = count
            winner = player
        break
print("the winner is player ", winner)
