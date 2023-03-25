# Arrange string characters such that lowercase letters should come first.
def lower_case_comeFirst(name):
    lst1=[]
    lst2=[]
    for ch in name:
        if ch.islower():
            lst1.append(ch)
        else :
            lst2.append(ch)
    lst3=''.join(lst1+lst2)
    print("The resultantString is: "+ lst3)


string = str(input("Enter a string: "))
lower_case_comeFirst(string)