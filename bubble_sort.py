'''compare element to the adjacent element to find the greater; then swap the 
   greater element with the smaller one. The process keeps on repeating till the greatest element is the
   last element of the list, the second greatest in the list is the second last element and so on...'''

# Initiating a list

n = int(input("Enter the number of elements in the list: "))
list1 = []      #Creating a empty list
for i in range(n):
    value = int(input("Enter the element in the list: "))
    list1.append(value)

# Impleting bubble sort execution pass

def bubble_sort(list1):
    for i in range(n):      # Number of passes| for n elements  it will make n-1 iterations| Pass- Every iterarion through each element of the list is called a pass
        for j in range(n-i-1):  # size -i-1 because last i elements are already sorted in previous passes
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]   # swapping of elements

# calling function
bubble_sort(list1)

# printing the sorted list
print("The sorted list is ...")
for i in range (n):
    print(list1[i], end = ' ')