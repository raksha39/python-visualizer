def bubble_sort(arr):
    n = len(arr)
    steps = []  # To store the steps for visualization

    for i in range(n):
        for j in range(0, n-i-1):
            # Record the current state of the array
            steps.append(arr.copy())
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Record the state after the swap
                steps.append(arr.copy())

    # Final state of the array
    steps.append(arr.copy())
    return steps  # Return the steps for visualization