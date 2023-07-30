Dic={"fast":"teez","tomorrow":"kal"
    ,"today":"aaj", "andic":{"fast":"teez","tomorrow":"suban"
    ,"today":"aaj"} }

# a=input("Options are:",Dic.keys)
# print("enter a word", Dic.get(a))
print(Dic["fast"])
print(Dic["andic"]["tomorrow"])
Dic["fast"]=["anotherdic"] #this will update the list
print(Dic)


# Dictionary Methods
Dic2={"fast":"teez","tomorrow":"kal"
    ,"today":"aaj",
    }

print(Dic2.keys())
print(list(Dic2.keys()))
print(type(Dic2.keys()))
print(Dic2.values())
print(Dic2.items())

updatedic2={"fast":"jaldi","khaleeque":"a boy"}
Dic2.update(updatedic2)
print(Dic2)

# print(Dic2["slow"])
print(Dic2.get("slow"))

#Sets
x={1,2,3,4,5}
print(type(x))
print(x)
#empty set
y=set()
print(type(y))
print(y)
#this will create empty dictionary not empty set
s={}
print(s)
print(type(s))

# Set Methods
a=set()
a.add(1)
a.add(2)
a.add(1)
print(a)
a.add((7,8)) #we can add tuple in set
print(a)

print(len(a))
a.remove(1)
print(a)
print(a.pop())#randomly removes items
a.clear()
print(a)