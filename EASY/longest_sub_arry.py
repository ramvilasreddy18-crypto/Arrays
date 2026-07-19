# # brute force approach
# arr = [1,2,3,1,1,1,4,2,3]
# target_sum = int(input("enter target sum : "))
# n = len(arr)
# maxi_len = 0
# for i in range(n):
#     for j in range(i,n):
#         s = 0
#         for k in range(i,j+1):
#             s += arr[k]
#         if s == target_sum:
#             maxi_len = max(maxi_len,j-i+1)
# print(maxi_len)
# better solution using hashing and it is optimal solution when it contains 0's and negative numbers
# arr = [1,2,3,1,1,1,4,2,3]
# k = int(input("enter target element : "))
# presummap = {}
# current_sum = 0
# maxlen = 0
# for i in range(len(arr)):
#     current_sum += arr[i]
#     if current_sum == k:#if subarray starts from 0 index
#         maxlen = max(maxlen,i+1)
#     rem = current_sum - k # we store remaning means total sum - the target element 
#     if rem in presummap: # we will check wheather the ele present in map if present current index - presum index 
#         length = i-presummap[rem]
#         maxlen = max(maxlen,length)
#     if current_sum not in presummap:
#         presummap[current_sum] = i
# print(maxlen)
# optimal solution
arr = [1,2,1,1,1]
k = 3
left = 0
right = 0
n = len(arr)
max_len = 0
current_sum = arr[0]
while right<n:
    while left<=right and current_sum>k:
        current_sum -= arr[left]
        left += 1
    if k == current_sum:
        max_len = max(max_len,right-left+1)
    right += 1
    if right<n:
        current_sum += arr[right]
print(max_len)