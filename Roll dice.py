# Roll dice 
import random
def roll(min,max):
    while True:
        print("<<...WELCOME TO ROLIING DICE ...>>")
        number = random.randint(min,max)
        print(f"your number : {number}")
        choice = input("DO YOU WANT TO PLAY AGAIN ? (y/n)")
        if choice.lower() == 'n':
             break
roll(1,5)