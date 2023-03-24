num = int (input("Enter the number: "))
fact= 1
for i in range(num,1,-1):
    fact*=i
print("factorial of {} is:".format(num), fact)
