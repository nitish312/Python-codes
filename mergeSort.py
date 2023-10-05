def merge(arr, start, mid, end):
    n1 = mid + 1 - start
    n2 = end - mid

    leftPart = [0] * n1
    rightPart = [0] * n2

    for i in range(0, n1):
        leftPart[i] = arr[start + i]
 
    for j in range(0, n2):
        rightPart[j] = arr[mid + 1 + j]

    i = 0
    j = 0
 
    while(i < n1 and j < n2):
        if(leftPart[i] <= rightPart[j]):
            arr[start] = leftPart[i]
            i += 1
        else:
            arr[start] = rightPart[j]
            j += 1
        start += 1

    while(i < n1):
        arr[start] = leftPart[i]
        i += 1
        start += 1

    while(j < n2):
        arr[start] = rightPart[j]
        j += 1
        start += 1

def mergeSort(arr, start, end):
    if(start >= end): return
    mid = (start + end) // 2;
    mergeSort(arr, start, mid)
    mergeSort(arr, mid + 1, end)
    merge(arr, start, mid, end)

arr = [60, 50, 40, 30, 20, 10]

print(arr)

mergeSort(arr, 0, len(arr) - 1)

print(arr)