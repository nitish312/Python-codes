def linearSearch(arr, ele):
    cnt = 0;
    for i in arr:
        if(i == ele):
            return cnt
        cnt += 1
    return -1

ele = 40

arr = [10, 20, 30, 40, 50, 60]

ind = linearSearch(arr, ele)

if ind == -1:
    print(f"{ele} not found")
else:
    print(f"{ele} found at index {ind}")

