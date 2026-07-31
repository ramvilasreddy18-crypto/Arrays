# brute force approach
# arr = [4,2,2,6,4]
# k = 6
# count = 0
# n = len(arr)
# for i in range(n):
#     for j in range(i,n):
#         xor = 0
#         for l in range(i,j+1):
#             xor ^= arr[l]
#         if xor == k:
#             count += 1
# print(count)
# better solution 
# arr = [4,2,2,6,4]
# k = 6
# count = 0
# n = len(arr)
# for i in range(n):
#     xor = 0
#     for j in range(i,n):
#         xor ^= arr[j]
#         if xor == k:
#             count += 1
# print(count)
# optimal solution
arr = [4,2,2,6,4]
k = 6
count = 0 
xr = 0
freq = {0:1}
for i in arr:
    xr ^= i
    x = xr^k
    if x in freq:
        count += freq[x]
    freq[xr] = freq.get(xr,0)+1
print(count)

