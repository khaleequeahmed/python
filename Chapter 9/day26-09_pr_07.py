content=True
i=1
with open("log.txt") as f:
    while content:
        content=f.readline()
        if "python" in content.lower():
            print(content)
            print(f"yes python is present in line no {i}")
        i+=1