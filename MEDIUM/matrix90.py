# it just prints the original matrix in this order
# n,m = map(int, input().split())
# arr = []
# for _ in range(n):
#     row = list(map(int,input().split()))
#     arr.append(row)
# for j in range(m):
#     for i in range(n-1,-1,-1):
#         print(arr[i][j],end=" ")
#     print()
# brute force approach 
n,m = map(int, input().split())
arr = []
ans = [[0]*n for _ in range(m)]
for _ in range(n):
    row = list(map(int,input().split()))
    arr.append(row)
for i in range(n):
    for j in range(m):
        ans[j][n-1-i] = arr[i][j]
for num in ans:
    print(*num)
# optimal code 
n,m = map(int, input().split())
arr = []
for _ in range(n):
    row = list(map(int,input().split()))
    arr.append(row)
for i in range(n-2):
    for j in range(i+1,m):
        arr[i],arr[j] = arr[j],arr[i]
for i in arr(m):
    arr[i].reverse()
for i in arr:
    print(*i)
