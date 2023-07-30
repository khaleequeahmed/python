## Create a list using []
a=[1,2,3,4,5]
print(a)
print(a[0:2])
print(a[4])
a[0]=6
print(a)
print(a.sort())

#List Slicing
b=["khaleeque","ahmed","jatoi",1,2]
print(b[0:1])
print(b[-3:])
print(b)

#list Methods
y=[1,2,3,5,6,7,9,8]
y.reverse()# Reverses the list
y.sort() # Sorts the list
y.append(12)# adds 12 at the end of the list
y.insert(0,500) #inserts (given number) 500 at index 0
y.pop(1)# Removes element at given index 
y.remove(2)#Removes first occurrence of value 100 from the element
print(y)

#Tuple
t=(1,)
print(type(t))

#tuple Methods
x=(1,2,3,4,1,5,6,1,7)
print(x.count(1))
print(x.index(3))