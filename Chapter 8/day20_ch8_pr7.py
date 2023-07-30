this = "    Khaleeque is a good boy    "
print(this)
print(this.strip()) #--> .strip will remove extra spaces 


def remove_and_split(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()
sentence = ("   My name is Khaleeque Ahmed     ")
k = remove_and_split(sentence, " Khaleeque")
print(k)