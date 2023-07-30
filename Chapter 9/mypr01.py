file1='b.txt'
file2='h.txt'

with open('b.txt', 'r') as f:
    f1=f.read()

with open('h.txt', 'r') as f:
    f2=f.read()

if (f1>f2):
    print("f1 is greater than f2")

else:
    print("f2 is greater than f1")