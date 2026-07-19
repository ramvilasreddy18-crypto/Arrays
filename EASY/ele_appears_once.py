# brute force approach
# arr = [1,1,2,3,3,4,4]
# n = len(arr)
# for i in range(n):
#     num = arr[i]
#     count = 0
#     for j in range(n):
#         if num == arr[j]:
#             count += 1
#     if count == 1:
#         print(num)
# optimal solution 
# arr = [1,1,2,3,3,4,4]
# freq = {}
# for num in arr:
#     freq[num] = freq.get(num,0)+1
# for key,value in freq.items():
#     if value == 1:
#         print(key)
#         break
# optimal solution
arr = [1,1,2,3,3,4,4]
xor = 0
for i in range(len(arr)):
    xor ^= arr[i]
print(xor)
