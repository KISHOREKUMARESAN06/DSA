def find_element_index(arr, x):
    try:
        return arr.index(x)
    except ValueError:
        return -1


arr = [1, 2, 3, 4]
x = 3
print(find_element_index(arr, x))

