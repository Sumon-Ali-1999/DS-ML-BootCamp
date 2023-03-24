sz=int(input("Enter the size of a list :"))#size of the list
lst=[] # an empty list declaration
print("Enter the value of the list: ")
for i in range(0,sz):
    num= float(input()) #float input
    lst.append(num) #appending into the list
print("The list is: ")
print(lst)