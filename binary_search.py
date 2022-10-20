stack = []
def binary_search(el,list):
    beg = 0
    end = len(list) - 1
    while beg<=end:
        mid = (beg+end)//2
        if el>list[mid]:
            beg = mid +1
        elif el<list[mid]:
            end = mid - 1
        else:
            return mid
    return -1

stack = []
stack = eval(input("Enter the elements of the list in sorted manner: "))
# print("The sorted list is",stack.sort())
el = int(input("Enter the element to look for in the list"))
result = binary_search(el,stack)
if result == -1:
    print("Element not in the list")
else:
    print("Element present in the list at ", result)