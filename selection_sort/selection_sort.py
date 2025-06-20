def selection_sort(nums):
    n = len(nums)  
    for i in range(n):
        minpos = i
        for j in range(i, n): 
            if nums[j] < nums[minpos]:
                minpos = j
        
        # Swap the elements
        nums[i], nums[minpos] = nums[minpos], nums[i]
        
        # Print each pass that occurrs in the loop
        print(f"Pass {i+1}: {nums}")

x = [33, 45, 12, 90, 2]
print(selection_sort(x))