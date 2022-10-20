import pickle
with open ("empfile1.dat", "ab") as f:
    recno = 1
    print("Enter the record of the employees: ")
    print()
    while True:
        print("RECORD NO.", recno)
        empname = input("Enter the name: ")
        empreg = int(input("Enter registration number: "))
        empsal = int(input("Enter the basic salary: "))
        empalow = int(input("Enter the allowance: "))
        total_sal = empsal + empalow
        data = [empname,empreg,empsal,empalow, total_sal]
        pickle.dump(data,f)
        ask = input('Enter more data? (Y/N')
        recno += 1
        if  ask.lower() == 'n':
            print("Record Entry Over")
            print()
            break

print("Now reading the employee records from the file...")
print()
readrec = 1
try:
    with open("empfile1.dat", "rb") as f:
        while True:
            a = pickle.load(f)
            print ("Record Number: ", readrec)
            print(a)
            readrec += 1
except EOFError:
    pass
