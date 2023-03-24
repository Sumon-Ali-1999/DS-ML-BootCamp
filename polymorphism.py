# print(4+5,"4"+"5")
a=4
print(a.__add__(5))
# print(a.__add__('5'))


#Method Overloading
class Employee:
    def __init__(self,name,): ## infinite value pass
        self.name=name
    
    def income(self,money=None):
        self.money= money
        if money == None:
            print(f"{self.name} is poor enough")
        elif money>50:
            print(f"{self.name} is not poor")
        else:
            print(f"{self.name} is rich")

me = Employee("Sumon")
me.income(95)