arr = [1,2,3,4,5,6]
temp = arr[0]
n = len(arr)
print(arr)
for i in range(1,n):
    arr[i-1] = arr[i]
arr[n-1] = temp
print(arr)