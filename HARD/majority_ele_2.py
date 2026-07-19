# brute force approach time complexity nearly O(n*n) 
# n = int(input())
# arr = list(map(int,input().split()))
# ans = []
# for i in range(n):
#     if len(ans) == 0 or ans[0]!=arr[i]:
#         count = 0
#         for j in range(n):
#             if arr[j] == arr[i]:
#                 count += 1
#         if n//3<count:
#             ans.append(arr[i])
#     if len(ans) == 2:
#         break
# print(ans)
# better solution tc = O(n) and sc = O(n)
# n = int(input())
# arr = list(map(int, input().split()))
# ans = []
# mpp = {}
# mn = n//3 + 1
# for num in arr:
#     if num not in mpp:
#         mpp[num] = 0
#     mpp[num] += 1
#     if mpp[num] == mn:
#         ans.append(num)
# print(ans)
# optimal solution moores voting algorithm
n = int(input())
arr = list(map(int, input().split()))
count1 = count2 = 0
ele1 = ele2 = None
for i in range(n):
    if count1 == 0 and ele2!=arr[i]:
        count1 = 1
        ele1 = arr[i]
    elif count2 == 0 and ele1!=arr[i]:
        count2 = 1
        ele2 = arr[i]
    elif ele1 == arr[i]:
        count1 += 1
    elif ele2 == arr[i]:
        count2 += 1
    else:
        count1 -= 1
        count2 -= 1
count1 = count2 = 0
for i in range(n):
    if ele1 == arr[i]:
        count1 += 1
    if ele2 == arr[i]:
        count2 += 1
ls = []
if count1>len(arr)//3:
    ls.append(ele1)
if count2>len(arr)//3 and ele1!=ele2 :
    ls.append(ele2)
ls.sort()
print(ls)