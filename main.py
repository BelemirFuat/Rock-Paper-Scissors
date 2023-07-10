import random

def play():
    user = input("R , P, S ?: ")
    computer = random.choice(['r','p','s'])
    print("Computer choose {}".format(computer))
    if user == computer:
        print("it is a tie")
    elif user == 'r':
        if computer == 'p':
            print("Computer won.")
        elif computer == 's':
            print("You won.")
    elif user == 'p':
        if computer=='r':
            print("you won.")
        elif computer =='s':
            print("Computer won.")
    elif user == 's':
        if computer == 'r':
            print("Computer won.")
        else:
            print("You won.")
    else:
        print("wrong.")

play()