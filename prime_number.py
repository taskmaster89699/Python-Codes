n1 = int(input("Enter the number to be checked if it is a prime number: "))
flag=0
if n1>1:
    for i in range(2,int(n1/2)):
        if n1%i == 0:
            flag = 1
            break
    if flag == 1:
        print(n1, 'is not a prime number')
    else:
        print(n1, 'is a prime number')
else:
    print("Invalid entry, enter a number greater than 0")