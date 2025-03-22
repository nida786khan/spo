def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

numbers = [1, 3, 5, 7, 9, 11, 15, 18, 21]
target = int(input("Enter number to search: "))

index = binary_search(numbers, target)
if index != -1:
    print(f"🎯 Found at index {index}")
else:
    print("❌ Not in the list")
