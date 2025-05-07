n = int(input("Enter the number"))


for i in range (2,n):
    if(n%i) == 0:
        print("number is not prime")
else :
    print("prime number")