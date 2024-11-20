def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


input_list = [14, 46, 43, 27, 57, 41, 45, 21, 70]
sorted_list = selection_sort(input_list)
print(sorted_list)
