#Strings Functions

story="Once upon a time there was a country in Europe called Yugoslavia"
print(len(story)) #len() --> #This will return the length of string

print(story.endswith ("Yugoslavia"))
print(story.endswith ("kghda"))

print(story.count ("a"))  #--> Counts the total number of occurence of any character
print(story.count ("was")) 

print(story.capitalize ()) #--> this capitalize() function capital the character

print(story.find ('Europe')) #--> this .find() function find a word and returns the index of first occurence

print(story)
print(story.replace ('Yugoslavia', 'East Germany'))

