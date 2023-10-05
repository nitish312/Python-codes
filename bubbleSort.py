def bubbleSort(arr):
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
arr = [60, 50, 40, 30, 20, 10]

print(arr)

bubbleSort(arr)

print(arr)