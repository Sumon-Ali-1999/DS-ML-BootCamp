# class Car:
#     area = 0
#     arr = [1,2]
#     def music(self):
#         run_the_music
#     def steering(self):
#         move_the_direction

# toyota = Car() #object
# premio = Car()
# #Method
# def add(a,b):
#     return a+b
# add(1+2)


# here self is a reference of the class
# class Calculator:
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
    
# calc = Calculator()
# s=calc.add(12,24)
# print(s)

#init 
class Calculator:
    def __init__(self,a,b): #dunder init# class constructor
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b
    def sub(self):
        return  self.a-self.b
    
calc = Calculator(12,24)
s=calc.add()
print(s)