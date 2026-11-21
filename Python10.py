import random
guessit=random.randint(1,20)

while True:
    guess=int(input("Guess a number between 1 and 20"))

    if guess==guessit:
        print("Yipee youre correct")
    elif guess>guessit:
        print("Its highhhhh")
    elif guess<guessit:
        print("Its too loowwww")
