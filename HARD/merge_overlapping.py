# brute force approach
# arr = [[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17],]
# arr.sort()
# ans = []
# n = len(arr)
# for i in range(n):
#     start = arr[i][0]
#     end = arr[i][1]
#     if len(ans) != 0 and end<=ans[-1][1]:
#         continue
#     for j in range(i+1,n):
#         if arr[j][0] <= end:
#             end = max(end,arr[j][1])
#         else:
#             break
#     ans.append([start,end])
# print(ans)
# optimal solution
arr = [[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17],]
arr.sort()
ans = []
n = len(arr)
for i in range(n):
    if not ans or arr[i][0]>ans[-1][1]:
        ans.append(arr[i])
    else:
        ans[-1][1] = max(ans[-1][1],arr[i][1])
print(ans) 

