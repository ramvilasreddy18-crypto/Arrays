arr = [1,1,1,1,1,1,1,1,1,1]
smallest = arr[0]
ssmallest = float('inf')
for i in range(1,len(arr)):
    if smallest>arr[i]:
        ssmallest = smallest
        smallest = arr[i]
    elif smallest != arr[i] and ssmallest>arr[i]:
        ssmallest = arr[i]
    elif ssmallest == float('inf'):
        print("no second largest")
        break
print(ssmallest)