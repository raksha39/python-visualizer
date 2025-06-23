def selection_sort(array):
    steps = []
    n = len(array)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
            steps.append(array.copy())  # Capture the state of the array after each comparison
        
        array[i], array[min_index] = array[min_index], array[i]  # Swap the found minimum element with the first element
        steps.append(array.copy())  # Capture the state of the array after each swap
    
    return steps  # Return the steps for visualization