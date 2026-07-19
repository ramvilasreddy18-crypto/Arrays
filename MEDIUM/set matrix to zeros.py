# # brute force approach 
# N,M = map(int, input().split())
# arr = []
# for _ in range(N):
#     row = list(map(int,input().split()))
#     arr.append(row)
# def markrow(i):
#     for j in range(M):
#         if arr[i][j] != 0:
#             arr[i][j] = -1
# def markcol(j):
#     for i in range(N):
#         if arr[i][j] != 0:
#             arr[i][j] = -1
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 0:
#             markrow(i)
#             markcol(j)
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == -1:
#             arr[i][j] = 0
# for row in arr:
#     print(*row)
# # better solution
N,M = map(int, input().split())
arr = []
for _ in range(N):
    row = list(map(int,input().split()))
    arr.append(row)
rows = [0]*N
cols = [0]*M
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            rows[i] = 1
            cols[j] = 1
for i in range(N):
    for j in range(M):
        if rows[i] == 1 or cols[j]==1:
            arr[i][j] = 0
for row in arr:
    print(*row)
# optimal solution
