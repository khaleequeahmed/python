# Use open fuction to read and write the content of a file but not working

# Write

f = open('sample.txt', 'w')
data = f.write("12") #--> Write anything in this it will write given into file
print(data)
f.close()

# write function will remove existing content and write given content 