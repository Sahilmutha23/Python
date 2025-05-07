n = int(input("enter number"))
n1 = int(input("enter number"))
n2 = int(input("enter number"))
n3 = int(input("enter number"))

if n>n1 and n>n2 and n>n3:
    print("Number 1 is greater",n)
elif n1>n and n1>n2 and n1>n3 :
    print("Number 2 is greater",n1)
elif n2>n and n2>n1 and n2>n3:
    print("number 3 is greater",n2)
else :
    print ("number 4 is greater",n3)

print("end of program ")
