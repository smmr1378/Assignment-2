import random
while True:
    dice = random.randint(1,6)
    if dice == 6:
        answer = random.randint(1,6)
        print("you can roll the dice again", answer)
    else:
        print ("your turn")
    break