n1 = int(input("Enter the number to find the factor of: "))
print(1, end = ', ')
fac = 2
while fac <= n1/2:
    if n1%fac == 0:
        print(fac, end =', ')
    fac +=1
