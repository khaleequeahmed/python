# marks = [30,40,50]
# percantage = (sum(marks)/300)*100

# marks2 = [50, 70, 60, 55]
# percantage2 = ((marks2[0] + marks2[1] + marks2[2] + marks2[3])/400)*100

# print(percantage,percantage2)

def percantage(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return p

marks1 = [30, 40, 50, 60]
percantage1 = percantage(marks1)

marks2 = [50, 70, 60, 55]

percantage2 = percantage(marks2)
print(percantage1,percantage2)


def fun():
    print("hello buddy")
kj=fun()

