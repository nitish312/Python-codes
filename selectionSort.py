def selectionSort(arr):
    n = len(arr)
    for i in range(0, n):
        minIndex = i
        for j in range(i + 1, n):
            if(arr[j] < arr[minIndex]):
                minIndex = j
        arr[minIndex], arr[i] = arr[i], arr[minIndex]

arr = [60, 50, 40, 30, 20, 10]

print(arr)

selectionSort(arr)

print(arr)