# #brute force approach
# arr = [1,0,2,3,2,0,0,4,5,1]
# n = len(arr)
# temp = [0]*n
# j = 0
# for i in range(n):
#     if arr[i] != 0:
#         temp[j] = arr[i]
#         j += 1
# j = 0
# for i in range(n):
#     arr[i] = temp[j]
#     j += 1
# print(arr)
# optimal
arr = [1,0,2,3,2,0,0,4,5,1]
print(arr)
n = len(arr)
j = -1
for i in range(n):# for finding 1st zero in the array
    if arr[i] == 0:
        j = i # store its index in j
        break
for i in range(j+1,n):
    if arr[i] != 0: # find non zero elements and swap with zeros
        arr[i],arr[j] = arr[j],arr[i]
        j += 1
print(arr)