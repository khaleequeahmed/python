# Use open function to read the content of a file

# f=open("sample.txt","r")
f=open("sample.txt") # by default the mode is r
data = f.read()
# data = f.read(9) # reads first 9 characters from the file 
print(data)
f.close()


# ye tab kaam kerega jab main us folder ko open with code kerke kholu
# jis main file bani hui ya banai ho warna agar main python folder hi main
# open with code kerke kholu ga to ye function python folder main 
# hi kaam kere ga na ki chapter 9 folder main
