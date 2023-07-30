Dictionary={"Pankha" : "Fan",
            "Taar" : "Cable",
            "Dabba" : "Box"}
print("Options are", Dictionary.keys())

a=input("Enter the Urdu word\n")
# # print("The meaning of your word is:", Dictionary[a])

# # Below line will not throw an error if the key is not present in dictionary
print("The meaning of your word is:", Dictionary.get(a))

