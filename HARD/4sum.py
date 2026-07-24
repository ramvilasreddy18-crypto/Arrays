# brute force solution
# n = int(input())
# arr = list(map(int,input().split()))
# ans = set()
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             for l in range(k+1,n):
#                 tot = arr[i]+arr[j]+arr[k]+arr[l]
#                 if tot == 0:
#                     temp = [arr[i],arr[j],arr[k],arr[l]]
#                     temp.sort()
#                     ans.add(tuple(temp))
# print(ans)
# better solution 
n = int(input())
arr = list(map(int,input().split()))
ans = set()
for i in range(n):
    for j in range(i+1,n):
        hashset = set()
        for k in range(j+1,n):
            fourth = -(arr[i]+arr[j]+arr[k])
            if fourth in hashset:
                temp = [arr[i],arr[j],arr[k],fourth]
                temp.sort()
                ans.add(tuple(temp))
            hashset.add(arr[k])
print(ans)
# optimal solution
n = int(input())
arr = list(map(int,input().split()))
target = int(input())
arr.sort()
for i in range(n):
    if i>0 and arr[i] == arr[i-1]:
        continue
    for j in range(i+1,n):
        if j>i+1 and arr[j] == arr[j-1]:
            continue
        k = j+1
        l = n-1
        while k<l:
            s = arr[i]+arr[j]+arr[k]+arr[l]
            if s == target:
                ans.append([arr[i],arr[j],arr[k],arr[l]])
                k+=1
                l-=1
                while k<l and arr[k] == arr[k-1]:
                    k+=1
                while k<l and arr[l] == arr[l+1]:
                    l-=1
            elif s>target:
                l-=1
            else:
                k+=1
print(ans)