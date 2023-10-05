def binarySearch(arr, ele):
    start = 0
    end = len(arr) - 1
    
    while(start <= end):
        mid = start + (end - start) // 2
        if(arr[mid] == ele):
            return mid
        elif(arr[mid] < ele):
            start = mid + 1
        else:
            end = mid - 1
    
    return -1

ele = 40

arr = [10, 20, 30, 40, 50, 60]

ind2 = binarySearch(arr, ele)

if ind2 == -1:
    print(f"{ele} not found")
else:
    print(f"{ele} found at index {ind2}")