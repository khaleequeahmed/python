class Number:
    def __init__(self,num):
        self.num=num


    def __add__(self,num2):
        print('lets add')
        return self.num + num2.num 
    
    def __sub__(self,num2):
        print('lets substract')
        return self.num - num2.num 
    
    def __mul__(self,num2):
        print('lets multiply')
        return self.num * num2.num
    
    def __truediv__(self,num2):
        print('lets divide')
        return self.num / num2.num



n1=Number(5)
n2=Number(2)
sum=n1+n2
sub=n1-n2
mul=n1*n2
div=n1/n2

print(sum)
print(sub)
print(mul)
print(div)