# # brute force approach
# n = int(input())
# arr = list(map(int, (input().split())))
# st = set()
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if (arr[i]+arr[j]+arr[k] == 0):
#                 temp = [arr[i],arr[j],arr[k]]
#                 temp.sort()
#                 st.add(tuple(temp))
# print(st)
# better solution
# n = int(input())
# arr = list(map(int, (input().split())))
# st = set()
# for i in range(n):
#     hashset = set()
#     for j in range(i+1,n):
#         third = -(arr[i]+arr[j])
#         if third in hashset:
#             temp = [arr[i],arr[j],third]
#             temp.sort()
#             st.add(tuple(temp))
#         hashset.add(arr[j])
# print(st)
# optimal solution
n = int(input())
arr = list(map(int, (input().split())))
arr.sort()
ans = []
for i in range(n):
    if i>0 and arr[i] == arr[i-1]:
        continue
    j = i+1
    k = n-1
    while j<k:
        s = arr[i]+arr[j]+arr[k]
        if s<0:
            j += 1
        elif s>0:
            k -= 1
        else:
            ans.append([arr[i],arr[j],arr[k]])
            j += 1
            k -= 1
            while j<k and arr[j] == arr[j-1]:
                j+=1
            while j<k and arr[k] == arr[k+1]:
                k-=1
print(ans)