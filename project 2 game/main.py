import random
randNumber = random.randint(1,100)
# print(randNumber)
userguess = None
guesses = 0 

while (userguess!=randNumber):
    userguess = int(input("Enter your guess\n"))
    guesses +=1
    if (userguess==randNumber):
        print("You guessed it correctly!")
    else:
        if (userguess>randNumber):
            print("You guessed it wrong!,Enter a smaller Number")
        else:
            print("You guessed it wrong!,Enter a larger Number")

print(f"You guessed the number in {guesses} guesses")

with open('hiscore.txt','r') as f:
    hiscore= int(f.read())

if (guesses<hiscore):
    print("You have just broken the HighScore")
    with open('hiscore.txt','w') as f:
        f.write (str(guesses))