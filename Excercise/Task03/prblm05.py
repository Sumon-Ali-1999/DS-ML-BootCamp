# Reverse a given string
def revstr(name):
    return name[::-1]
string = str(input("Enter a string: "))
reverse=revstr(string)
print("The reverse of that string is:",reverse)
