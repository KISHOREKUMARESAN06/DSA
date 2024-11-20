def lexicographical_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


input_names = ["Steve", "Alice", "bob", "Charlie", "dave"]
sorted_names = lexicographical_sort(input_names)
print(sorted_names)
