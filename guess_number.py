import random
number_of_guesses = 0
computer_number = random.randint(10,40)
while True:
    user_number = int(input("Enter your guess: "))

    if computer_number == user_number:
        print("number_of_guesses: ", number_of_guesses)
        print("you win")
        break
    elif computer_number > user_number:
        number_of_guesses = number_of_guesses + 1
        print("go up")
    elif computer_number < user_number:
        number_of_guesses = number_of_guesses + 1
        print("go down")