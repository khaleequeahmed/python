with open("log.txt") as f:
    content = f.read()#.lower()

if 'python' in content.lower():
    print("Yes Python is present in log file")
else:
    print("No Python is not present in log file")