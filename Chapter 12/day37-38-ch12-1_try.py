while(True):
    print("Press 'q' to quit")
    a = input("Enter a number: ")
    if a == "q":
        break
    try:
        print("trying...")
        a = int(a)
        if a>6:
            print("You Entered a Number greater than 6")
        else:
            print("You Entered a Number lesser than 6")
    except Exception as e:
        print(f'Your input resulted in an error {e}')
print("Thanks for playing this game")