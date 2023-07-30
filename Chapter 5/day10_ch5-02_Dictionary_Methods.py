myDict={
    "fast" : "In a quick manner",
    "khaleeque" : "A coder",
    "marks" : [1,2,3,4,5],
    "anotherdict" : {"Khaleeque" : "A boy"},
    1:2
}

#Dictionary Methods

print(myDict.keys())
print(type(myDict.keys()))
print(list(myDict.keys())) #Prints the keys of the dictionary

print(myDict.values()) 

print(myDict.items()) #Prints the (key,value) for all content of the dictionaries
print(myDict)

updatedict={"ateeque":"brother",
            "barkat":"brother",
            "khaleeque":"men"} #if i wrote existing key then this function (update.()) will update existing key 
myDict.update(updatedict) #Update the dictionary by adding key-value from updatedict
print(myDict)

print(myDict.get("Marks2")) # Prints value associated with Marks2
# print(myDict["Marks2"]) # Prints value associated with Marks2

# What is the Difference between .get and [] in syntax dictionaries?

# print(myDict.get("Marks2")) # throws an none as Marks2 is not present in the dictionary
# print(myDict["Marks2"]) # throws an error as Marks2 is not present in the dictionary