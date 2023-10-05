def reverseArr(arr):
    start = 0
    end = len(arr) - 1
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
arr = [10, 20, 30, 40, 50, 60]

print(arr)

reverseArr(arr)

print(arr)