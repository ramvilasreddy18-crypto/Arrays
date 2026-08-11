# brute force solution using extra space
arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]
n = len(arr1)
m = len(arr2)
arr3 = [0]*(n+m)
left = 0
right = 0
index = 0
while left<n and right<m:
    if arr1[left]<=arr2[right]:
        arr3[index] = arr1[left]
        index += 1
        left += 1
    else:
        arr3[index] = arr2[right]
        index += 1
        right += 1
while n>left:
    arr3[index] = arr1[left]
    index += 1
    left += 1
while m>right:
    arr3[index] = arr2[right]
    right += 1
    index += 1
for i in range(n+m):
    if i<n:
        arr1[i] = arr3[i]
    else:
        arr2[i-n] = arr3[i]
print(*arr1,*arr2)
# with out extra space
arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]
n = len(arr1)
m = len(arr2)
left = n-1
right = 0
while left>=0 and right<m:
    if arr1[left] > arr2[right]:
        arr1[left],arr2[right] = arr2[right],arr1[left]
        left -= 1
        right += 1
    else:
        break
arr1.sort()
arr2.sort()
print(arr1,arr2)
# optimal solution shell sort
arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]
n = len(arr1)
m = len(arr2)
length = n+m
gap = (length+1)//2
while gap>0:
    left = 0
    right = gap+left
    while length>right:
        if left>=n:
            if arr2[left-n]<arr2[right-n]:
                arr2[left-n],arr2[right-n] = arr2[right-n],arr2[left-n]
        elif left<n and right>=n:
            if arr1[left]<arr2[right-n]:
                arr1[left],arr2[right-n] = arr2[right-n],arr1[left]
        else:
            arr1[left],arr1[right] = arr1[right],arr1[left]
        left += 1
        right += 1
    if gap == 1:
        break
    gap = (gap+1)//2
print(arr1,arr2)


