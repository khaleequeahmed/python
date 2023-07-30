myDict={
    "Fast" : "In a quick manner",
    "Khaleeque" : "A coder",
    "Marks" : [1,2,3,4,5],
    "anotherdict" : {"Khaleeque" : "A boy" , "hi" : "greeting" }
}


print(myDict["Fast"])
print(myDict["Khaleeque"])
myDict["Marks"]=[23,25,27] #this will update the list
myDict["k"]=[23,25,27] #this will update the list
print(myDict["Marks"])
print(myDict["anotherdict"])
print(myDict["anotherdict"]["Khaleeque"])

print(myDict)


