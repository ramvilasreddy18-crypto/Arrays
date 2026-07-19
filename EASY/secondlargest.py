arr = [1,2,4,7,7,5]
largest = arr[0]
slargest = -1
for i in range(1,len(arr)):
    if largest<arr[i]:
        slargest = largest
        largest = arr[i]
    elif largest != arr[i] and slargest<arr[i]:
        slargest = arr[i]
print(slargest)