import time
import sys
import random

play = True
while play:
    def delay(text):
        for c in text:
            sys.stdout.write(c)
            time.sleep(0.1)


    def guess_game(a):
        if a == 10:
            delay("\nEntering... Easy Mode")
            time.sleep(1)
            print("\nFirst to reach 10 guesses loses")
        elif a == 15:
            delay("\nEntering... Medium Mode")
            time.sleep(1)
            print("\nFirst to reach 15 guesses loses")
        elif a == 30:
            delay("\nEntering... Hard Mode")
            time.sleep(1)
            print("\nFirst to reach 30 guesses loses")

        score_1 = 0
        score_2 = 0
        for i in range(3):
            delay("\n\n\n\n\n\n\n\n\nRound ")
            print(i + 1)
            counter_total_1 = 0
            counter_total_2 = 0
            current_turn = 1
            time.sleep(1)
# start of game play
            while (counter_total_1 < a) or (counter_total_2 < a):
                if current_turn == 1:
                    print("\nPlayer One")
                elif current_turn == -1:
                    print("\nPlayer Two")
                time.sleep(1)

                counter = 0
                game = True
                if a == 10:
                    num = int(random.randrange(1, 10))
                    answer = input('Choose a number between 1-10 \n')
                elif a == 15:
                    num = int(random.randrange(1, 20))
                    answer = input('Choose a number between 1-20 \n')
                elif a == 30:
                    num = int(random.randrange(1, 100))
                    answer = input('Choose a number between 1-100 \n')

                while game:
                    if answer < num:
                        answer = input("Higher  (^-^)\n")
                        counter += 1
                    elif answer > num:
                        answer = input("Lower  (._.)\n")
                        counter += 1
                    elif answer == num:
                        print("Congrats! You got it!  b(^.^)d\n")
                        game = False
                        counter += 1
                        print("Number of guesses:")
                        print(counter)
                        if current_turn == 1:
                            counter_total_1 = counter_total_1 + counter
                        elif current_turn == -1:
                            counter_total_2 = counter_total_2 + counter
# check
                if counter_total_1 >= a or counter_total_2 >= a:
                    break
                current_turn *= -1
                delay("\n\n\n\n\n\n\n\n\n\n")

            delay("\n\n\n\n\n\n\n\n\n\n")
            print("\nPlayer One's total number of guesses:")
            print(counter_total_1)
            time.sleep(1)
            print("\nPlayer Two's total number of guesses:")
            print(counter_total_2)
            time.sleep(1)
            delay("\n\n")
# round end
            if counter_total_1 >= a and counter_total_2 < counter_total_1:
                delay("\nPlayer Two wins this round!")
                score_2 += 1
            elif counter_total_2 >= a and counter_total_1 < counter_total_2:
                delay("\nPlayer One wins this round!")
                score_1 += 1
# declare winner
        delay("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("And after 3 rounds... the winner is...")
        time.sleep(1)
        if score_1 > score_2:
            delay("Player... ONE!  ~(^o^)~")
        elif score_1 < score_2:
            delay("Player... TWO!  ~(^o^)~")
        delay("\nCongratulations!  \(^-^)/")


    def difficulty():
        invalid = True
        while invalid:
            decision = input('\nChoose difficulty: \n'
                             '\n1. Easy'
                             '\n2. Medium'
                             '\n3. Hard \n')
            if decision == 1:
                guess_game(10)
                invalid = False
            elif decision == 2:
                guess_game(15)
                invalid = False
            elif decision == 3:
                guess_game(30)
                invalid = False
            else:
                delay("That is not a valid difficulty. Please choose again. \n")
                delay("\n\n\n\n\n\n\n")

# start
    print("\n(~^-^)~   =-=-= Welcome to the Guessing Game! =-=-=   ~(^-^~)")
    time.sleep(1)
    print("\nFirst one to win 3 rounds wins!")
    time.sleep(1)
    difficulty()

# repeat
    not_valid = True
    while not_valid:
        delay("\n\n\n\n\n\n\n\n\n\n")
        choice = raw_input("\n\nWould you like to play again? [Y/N] \n")
        if (choice == "Y") or (choice == "y"):
            not_valid = False
        elif (choice == "N") or (choice == "n"):
            play = False
            not_valid = False
            delay("\n\nThanks for playing!  \(^-^)/ \n")
        else:
            delay("That is not a valid answer. Please choose again. \n")
