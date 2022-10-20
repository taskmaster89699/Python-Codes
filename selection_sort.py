'''In this method of sorting, in the first pass, all the elements in the unsorted list are traversed to find
    out the smallest element. The smallest element is then moved to the leftmost position in the list. In the 
    next pass, remaining elements are considered for finding the second smallest item in the list and is moved
    to the second place from the left. This process is continued till all the elements are arranged. '''

# initializing the list 
n = int(input("Enter the number of elements in the list: "))
list1 = []
for i in range(n):
    val = int(input("Enter the element in the list: "))
    list1.append(val)

# Performing selection sort execution pass
def selection_sort(list1):
    m = len(list1)
    flag = 1    #to decide when to swap
    for i in range(m):
        min = i     #defining the smallest element
        for j in range(i+1, m):     #since the smallest element is defined already and the rest elements are reduced by 1
            if list1[j]<list1[min]:
                min = j     # new minimum value
                flag = 1        #swap now
            if flag == 1:
                list1[min],list1[i] = list1[i],list1[min]       #elements swapped

selection_sort(list1)

#printing the sorted list
print("The sorted list is: ")
for i in range(n):
    print(list1[i], end=" ")
