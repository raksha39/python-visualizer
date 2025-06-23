def linear_search(arr, target):
    steps = []
    for i in range(len(arr)):
        steps.append({
            'array': arr.copy(),
            'current_index': i,
            'target': target,
            'found': arr[i] == target,
            'algorithm': 'Linear Search'
        })
        if arr[i] == target:
            break
    return steps