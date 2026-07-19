# # brute force approach
# arr1 = [1,2,2,3,3,4,5,6]
# arr2 = [2,3,3,5,6,6,7]
# vis = [0]*len(arr2)
# intersection = []
# for i in range(len(arr1)):
#     for j in range(len(arr2)):
#         if arr1[i] == arr2[j] and vis[j]==0:
#             intersection.append(arr1[i])
#             vis[j] = 1
#             break
#         if arr2[j]>arr1[i]:
#             break
# print(intersection)
# optimal solution
arr1 = [1,2,2,3,3,4,5,6]
arr2 = [2,3,3,5,6,6,7]
inter = []
i = 0
j = 0
while i<len(arr1) and j<len(arr2):
    if arr1[i]>arr2[j]:
        j += 1
    elif arr1[i]<arr2[j]:
        i += 1
    else:
        inter.append(arr1[i])
        i += 1
        j += 1
print(inter)
