class Calculator: #parent class

    def add(self ,a,b):
        return a+b
    def sub(self,a,b):
        return  a-b
    def sqr(self,a):
        return a*a
    
class Square(Calculator): #child class
    def sqr(self,a):
        return a*a
    
my_calc= Square()
ss = my_calc.add(12,24)
print(ss)
