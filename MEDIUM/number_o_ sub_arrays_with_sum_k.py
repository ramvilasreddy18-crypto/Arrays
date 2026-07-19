# brute force approach
# n = int(input())
# arr = list(map(int, input().split()))
# k = int(input())
# count = 0
# for i in range(n):
#     for j in range(i,n):
#         tot = 0
#         for z in range(i,j+1):
#             tot += arr[z]
#         if tot == k:
#             count += 1
# print(count)
# better solution
# n = int(input())
# arr = list(map(int, input().split()))
# k = int(input())
# count = 0
# for i in range(n):
#     tot = 0
#     for j in range(i,n):
#         tot += arr[j]
#         if tot == k:
#             count += 1
# print(count)
# optimal solution
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
mpp = {0:1}
presum = 0
count = 0 
for num in arr:
    presum += num
    remove = presum-k
    count += mpp.get(remove,0)
    mpp[presum] = mpp.get(presum,0) + 1
print(count)