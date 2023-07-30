import random
def gamewin(comp,you):
    if comp==you:
        return None
    
    elif comp=="r":
        if you=="s":
            return False
        elif you == "p":
            return True
    
    elif comp=="s":
        if you=="p":
            return False
        elif you=="r":
            return True

    elif comp=="p":
        if you=="r":
            return False
        elif you=="s":
            return True 




print("Comp Turn: Rock(r) Scissor(s) or Paper(p) ?")
randno = random.randint(1, 3)
if randno==1:
    comp="r"
elif randno==2:
    comp="s"
elif randno==3:
    comp="p"

you=(input("Your Turn: Rock(r) Scissor(s) or Paper(p) ?"))

print(f"Computer Choose {comp}")
print(f"You Choose {you}")

a = gamewin(comp,you)
 
if a == None:
    print("The Game is a Tie")
elif a:
    print("You Win")
else:
    print("You Lose")