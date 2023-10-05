def partition(arr, start, end):
    pivotEle = arr[start]
    cnt = 0
    for i in range(start + 1, end + 1):
        if arr[i] < pivotEle:
            cnt += 1

    pivotIndex = start + cnt
    arr[pivotIndex], arr[start] = arr[start], arr[pivotIndex]

    i = start
    j = end
    while(i < pivotIndex & j > pivotIndex):
        while(arr[i] < pivotEle): i += 1
        while(arr[j] > pivotEle): j -= 1
        if(i < pivotIndex & j > pivotIndex):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    return pivotIndex

def quickSort(arr, start, end):
    if(start >= end): return
    p = partition(arr, start, end)

    quickSort(arr, start, p - 1)
    quickSort(arr, p + 1, end)


arr = [60, 50, 40, 30, 20, 10]

print(arr)

quickSort(arr, 0, len(arr) - 1)

print(arr)