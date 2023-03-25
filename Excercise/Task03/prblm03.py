# Count all letters, digits, and special symbols from a given string

def count(name):
    alphabet=digit=special=0
    for ch in name:
        if ch.isalpha():
            alphabet+=1
        elif ch.isdigit():
            digit+=1
        else:
            special+=1
    print("Char:",alphabet,"Digits:",digit,"Symbol:",special)
string = str(input("Enter a string: "))
count(string)
