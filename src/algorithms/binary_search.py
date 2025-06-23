def binary_search(arr, target):
    steps = []
    # First sort the array for binary search
    arr.sort()
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        steps.append({
            'array': arr.copy(),
            'left': left,
            'right': right,
            'mid': mid,
            'target': target,
            'found': arr[mid] == target,
            'algorithm': 'Binary Search'
        })
        
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return steps