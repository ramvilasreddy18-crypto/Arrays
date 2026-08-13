# brute force soln
arr = [2,3,-2,4]
maxi = float('-inf')
n = len(arr)
for i in range(n):
    for j in range(i,n):
        prod = 1
        for k in range(i,j):
            prod *= arr[k]
        maxi = max(maxi,prod)
print(maxi)
# better solution
arr = [2,3,-2,4]
maxi = float('-inf')
n = len(arr)
for i in range(n):
    prod = 1
    for j in range(i,n):
        prod *= arr[j]
        maxi = max(maxi,prod)
print(maxi)
# optimal solution
arr = [2,3,-2,4]
prefix = suffix = 1
n = len(arr)
maxi = float('-inf')
for i in range(n):
    if prefix == 0:
        prefix = 1
    if suffix == 0:
        suffix = 1
    prefix *= arr[i]
    suffix *= arr[n-i-1]
    maxi = max(maxi,max(prefix,suffix))
print(maxi)