import random

def gamewin(comp,you):
    if comp==you:
        return None
    
    elif comp=="rock":
        if you=="scissor":
            return False
        elif you=="paper":
            return True
        
    elif comp=="paper":
        if you=="rock":
            return False
        elif you=="scissor":
            return True
        
    elif comp=="scissor":
        if you=="paper":
            return False
        elif you=="rock":
            return True



print("Comp Turn: Rock(rock) Paper(paper) or Scissor(scissor) ?")
rand=random.randint(1 ,3)
if rand==1:
    comp="rock"
elif rand==2:
    comp="paper"
elif rand==3:
    comp="scissor"



you=(input("Your Turn: Rock(rock) Paper(paper) or Scissor(scissor) ?:"))

print(f"Computer Choose {comp}")
print(f"You Choose {you}")

a = gamewin(comp,you)
if a == None:
    print("The Game is a tie")

elif a:
    print("You Win")

else:
    print("You Lose")