text = input("Enter the Text\n")
if ("make a lot of money" in text):
    spam=True
elif ("click this link" in text):
    spam=True
elif ("buy now" in text):
    spam=True
else:
    spam=False
if (spam):
    print("This is Spam")
else:
    print("This is not spam")