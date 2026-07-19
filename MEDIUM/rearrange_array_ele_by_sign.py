# brute force approach
# arr = [3,1,-2,-5,2,-4]
# pos = []
# neg = []
# n = len(arr)
# for i in range(n):
#     if arr[i]>=0:
#         ele = arr[i]
#         pos.append(ele)
#     else:
#         ele1 = arr[i]
#         neg.append(ele1)
# j = 0
# k = 0
# for i in range(n):
#     if i%2 == 0:
#         arr[i] = pos[j]
#         j += 1
#     else:
#         arr[i] = neg[k]
#         k += 1
# print(arr)
# optimal solution
arr = [3,1,-2,-5,2,-4]
pos = 0
neg = 1
n = len(arr)
ans = [None]*len(arr)
for i in range(n):
    if arr[i]>0:
        ans[pos] = arr[i]
        pos += 2
    else:
        ans[neg] = arr[i]
        neg += 2
print(ans)