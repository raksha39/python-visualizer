def merge_sort(arr):
    steps = []
    
    def merge_sort_helper(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid + 1, right)
            
            merge(arr, left, mid, right, steps)
    
    def merge(arr, left, mid, right, steps):
        # Create temp arrays
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
            steps.append(arr.copy())
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            steps.append(arr.copy())
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
            steps.append(arr.copy())
    
    merge_sort_helper(arr, 0, len(arr) - 1)
    return steps