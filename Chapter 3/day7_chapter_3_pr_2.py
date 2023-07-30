#problem no 2
letter = '''Dear <|Name|>,
Iam happpy to tell you about your Selection,
You are Selected
Regards: Khaleeque Ahmed
date: <|Date|>'''
name=input("Enter your Name\n")
date=input("Enter Date\n")
letter=letter.replace("<|Name|>", name)
letter=letter.replace("<|Date|>", date)
print(letter)

