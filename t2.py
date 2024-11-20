def next_greater_element(arr):
    result = []
    stack = []  
 
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(arr[i])
    
    return result[::-1]


arr = [4, 5, 2, 25]
output = next_greater_element(arr)
print(output)