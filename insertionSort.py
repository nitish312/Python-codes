def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        curr = arr[i]
        j = i - 1
        while (j >= 0 & curr < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr

arr = [60, 50, 40, 30, 20, 10]

print(arr)

insertionSort(arr)

print(arr)