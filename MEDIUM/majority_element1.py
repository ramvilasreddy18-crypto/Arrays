# # brute force approach
# arr = [2,2,3,1,1,2,2,2,1,2,3,2,]
# n = len(arr)
# for i in range(n):
#     count = 0
#     for j in range(n):
#         if arr[i] == arr[j]:
#             count += 1
#     if count>n//2:
#         print(arr[i])
#         break
# better using hash map
# arr = [2,2,3,1,2,2,2,2,1,2,3,2,]
# hash_map = {}
# n = len(arr)
# for i in arr:
#     hash_map[i] = hash_map.get(i,0)+1
# for key,value in hash_map.items():
#     if value>n//2:
#         print(key)
# optimal solution (MOORES VOTING ALGORITHM)
arr = [7,7,5,5,5,2,2,2,5,5,5,5,5]
count = 0
n = len(arr)
for i in range(n):
    if count == 0:
        count = 1
        ele = arr[i]
    elif arr[i] == ele:
        count += 1
    else:
        count -= 1
count1 = 0
for i in range(n):
    if ele == arr[i]:
        count1 += 1 
if count1>n//2:
    print(ele)
else:
    print("no majority ele ")