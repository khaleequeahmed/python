# Creating set in python
b=set()
print(b)
print(type(b))

#Adding Values to an empty set
b.add(1)
b.add(2)
b.add(3) #adding a value repeatedly does not change a set
b.add(3)
b.add(3)

b.add((6,7,8)) # we can add tuple in set
# b.add([5,6,7]) #We can not add list in set
# b.add({"khaleeque":"a boy"}) #we cannot add dictionary in set

# length of set
print(b)
print(len(b)) #Prints the length of set

# Removal of an item
b.remove(2) #removes 2 from set
# b.remove(15) --> #throws an error while trying to remove 15 (which is not present in set)
print(b)

print(b.pop()) #.pop will remove random item
print(b)
b.clear() #--> This function will clear set
print(b)