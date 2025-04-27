import random

target=random.randint(1,100)



while True:
    Guess=input("GUESS THE NUMBER OR QUIT(Q): ")
    if Guess=="Q":
        break
    Guess=int(Guess)
    if Guess==target:
        print("Sucess: correct guess!!")
        break

    elif Guess<target:
        print(" Your Guess is Quite Small Than The Target. TRY AGAIN ")
        

    else:
        print("Your Guess Is Quite Big Than Thwe Target. TRY AGAIN ")

print("-----GAME OVER-----")    