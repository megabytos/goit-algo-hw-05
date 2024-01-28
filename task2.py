def binary_search_upper_bound(arr, x):
    i = 0
    low = 0
    high = len(arr) - 1
    mid = 0
    upper_bound = arr[-1]

    if upper_bound < x:
        return -1

    while low <= high:
        i += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1        
        elif arr[mid] > x:
            upper_bound = mid
            high = mid - 1        
        else:
            return (i, mid)
   
    return (i, upper_bound)


if __name__ == '__main__':
    arr = [3.15, 4.45, 10.789, 42.44, 48.38, 56.45, 77.7, 80.80, 281.33, 842.50, 850.70, 860.30]

    print(binary_search_upper_bound(arr, 6))
    print(binary_search_upper_bound(arr, 60))
    print(binary_search_upper_bound(arr, -5))
    print(binary_search_upper_bound(arr, 42))
    print(binary_search_upper_bound(arr, 154))
    print(binary_search_upper_bound(arr, 854))
    print(binary_search_upper_bound(arr, 56.45))    
    print(binary_search_upper_bound(arr, 999))