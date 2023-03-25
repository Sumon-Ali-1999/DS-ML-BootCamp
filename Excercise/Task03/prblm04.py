# Split a string on hyphens.

def splitstr(name):
    print("splitted sting is: ")
    for i in range(len(name)):
        if name[i]=='-':
            print()
            continue
        else:
            print(name[i],end='')
string = str(input("Enter a string: "))
splitstr(string)
