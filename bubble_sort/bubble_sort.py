def bubble_sort(unsorted_list):
    
    n = len(unsorted_list)
    
    # Traverse through all list elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    
    return unsorted_list
x = [30,45,7,2,34]
print(bubble_sort(x))
