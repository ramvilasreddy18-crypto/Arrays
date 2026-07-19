arr = [3,2,1]
n = len(arr)
ind = -1
# find the break point of the array
for i in range(n-2,-1,-1):
    if arr[i]<arr[i+1]:
        ind = i
        break
# base case
if ind == -1:
    arr.reverse()
    print(arr)
# find next greater ele and swap note slightly grater than ind
for i in range(n-1,ind,-1):
    if arr[i]>arr[ind]:
        arr[ind],arr[i] = arr[i],arr[ind]
        break
# reverse the remaininig ele
arr[ind+1:] = reversed(arr[ind+1:])
print(arr)


