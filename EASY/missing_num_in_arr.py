# brute force approach 
# arr = [5,4,1,2,0]
# for i in range(len(arr)+1):
#     flag = 0
#     for j in range(len(arr)):
#         if arr[j] == i:
#             flag = 1
#             break
#     if flag == 0:
#         print(i)
#         break
# better solution
# arr = [5,4,1,2,0]
# hash_arr = [0]*(len(arr)+1)
# for num in arr:
#     hash_arr[num] = 1
# for i in range(len(hash_arr)):
#     if hash_arr[i] == 0:
#         print(i)
#         break
# optimal solution
# arr = [5,4,1,2,0]
# n = len(arr)
# total = int((n*(n+1)//2))
# s = 0
# for i in arr:
#     s += i
# res = total - s
# print(res)
# optimal solution than above one 
# xor1 = 0
# xor2 = 0
# arr = [5,4,1,2,0]
# n = len(arr)
# for i in range(n+1):
#     xor1 ^= i
# for i in arr:
#     xor2 ^= i
# print(xor1^xor2)
#optimal sol
xor1 = 0
xor2 = 0
arr = [5,4,1,2,0]
n = len(arr)
for i in range(n):
    xor1 ^= (i+1)
    xor2 ^= arr[i]
print(xor1^xor2)

