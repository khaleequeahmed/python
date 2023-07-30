#String Slicing
a=("khaleeque")
print(a[0:5])
print(a[0])

#String slicing with skip sequences
f1="khaleeque"
print(f1[0::2])

b=("khaleeque ahmed")
print(b[3:])
print(b[-4:])

#Concatenating two String
k="khaleeque"
c="hi, "
print(c+k)

#String
hc="khaleeque's"
print(hc)

#Escape Sequence
Story=("When i was a kid i played alot gta san andreas sa")
Story2=("When i was a kid\n\ti played alot gta san andreas\\sa")
print(Story)
print(Story2)

# String Methods
Story3=("once upon a time i was kid")
print(len(Story3))
print(Story3.endswith("d"))
print(Story3.find("upon"))
print(Story3.replace("kid","child"))
print(Story3.count("i"))
print(Story3.capitalize())
