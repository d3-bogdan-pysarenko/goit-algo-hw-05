def binary_search_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] >= target:
            upper_bound = arr[mid] # upper bound candidate
            right = mid - 1 # looking for lowe but ≥ target
        else:
            left = mid + 1  # looking forgreater value

    return iterations, upper_bound


# checking time
array = [1.2, 1.3, 1.9, 2.5, 3.7, 3.7, 5.0, 8.4, 9.6]
print(binary_search_upper_bound(array, 3.7))
print(binary_search_upper_bound(array, 9.9))
print(binary_search_upper_bound(array, 1.1))
print(binary_search_upper_bound(array, 1.21))