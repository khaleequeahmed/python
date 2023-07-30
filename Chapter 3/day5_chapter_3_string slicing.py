greeting=("good morning, ")
name=("khaleeque")
print(type(name))
print(greeting+name)
# -->Concatenating two String
c=greeting+name
print(c)

name=("khaleeque")
print(name[0])
# name [3] = "d" #--> Does not work

#String Slicing
print(name[0:2]) #ye 2 ko nahi giney ga,String slicing main akhri wale number ko nahi giny ga
print(name[5:7])

print(name[:5]) #is same as (k[0:5])
print(name[0:]) #is same as (k[0:5])]
#Negative index
c=name[-9:] #is same as (c[0:9]) ye -1 ko nahi giney ga,String slicing main akhri wale number ko nahi giny ga
print(c)