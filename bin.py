# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             return mid  # Return the index
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1  # Target not found


# # Example
# arr = [2, 5, 8, 12, 16, 23, 38, 56]
# target = 23

# result = binary_search(arr, target)

# if result != -1:
#     print(f"Element found at index {result}")
# else:
#     print("Element not found")






#include <stdio.h>

arr = [2, 4, 6, 8, 10, 12, 14, 16]
key = 10

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at index", mid)
        break
    elif key < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1
else:
    print("Element not found")