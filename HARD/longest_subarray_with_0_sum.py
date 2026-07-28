# brute force approach
# arr = [15,-2,2,-8,1,7,10,23]
# maxi = float('-inf')
# for i in range(len(arr)):
#     tot = 0
#     for j in range(i,len(arr)):
#         tot += arr[j]
#         if tot == 0:
#             maxi = max(maxi,j-i+1)
# print(maxi)
# better solution
arr = [15,-2,2,-8,1,7,10,23]
tot = 0
maxi = 0
map = {}
for i in range(len(arr)):
    tot += arr[i]
    if tot == 0:
        maxi = i+1
    elif tot in map:
        maxi = max(maxi,i-map[tot])
    else:
        map[tot] = i
print(maxi)
