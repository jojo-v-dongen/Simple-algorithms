def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return "Item found", i
    return "Item not found"
