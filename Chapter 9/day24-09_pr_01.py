f = open("poem.txt")
k = f.read()
if "twinkle" in k:
    print("Twinkle is present in peom")
else:
    print("Twinkle is not present in poem")
f.close()