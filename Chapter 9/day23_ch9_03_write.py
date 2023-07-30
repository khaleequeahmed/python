# Write

f = open("another.txt", "w") 
f.write("Iam ") #--> if i write something in it, it will overwrite the file
f.write(" Iam Writing") #it can be called multiple times
f.write(" Iam Writing")
f.write("\nIam not Writing")
f.close

