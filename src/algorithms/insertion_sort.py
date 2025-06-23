def insertion_sort(arr):
    steps = []  # To store the steps for visualization
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            steps.append(arr.copy())  # Capture the state after each move
            j -= 1
        arr[j + 1] = key
        steps.append(arr.copy())  # Capture the state after inserting the key

    return steps  # Return the steps for visualization