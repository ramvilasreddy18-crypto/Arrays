# brute force approach
# arr = [102,4,100,1,101,3,2,1,1]
# longest = 1
# def linear(arr,num):
#     for i in range(len(arr)):
#         if arr[i] == num:
#             return True
#     return False
# for i in range(len(arr)):
#     x = arr[i]
#     count = 1
#     while linear(arr,x+1)==True :
#         x += 1
#         count += 1
#     longest = max(count,longest)
# print(longest)
# better solution
# arr = [102,4,100,1,101,3,2,1,1]
# arr.sort()
# longest = 1
# count = 0
# last_smaller = float('-inf')
# for i in range(len(arr)):
#     if arr[i]-1 == last_smaller:
#         count += 1
#         last_smaller = arr[i]
#     elif arr[i]!= last_smaller:
#         count = 1
#         last_smaller = arr[i]
#     longest = max(count,longest)
# print(longest)
# optimal solution
arr = [102,4,100,1,101,3,2,1,1]
st = set(arr)
longest = 0
for num in st:
    if num-1 not in st: # if the previous num is not there in set it is starting point in set
        count = 1
        x = num
        while x+1 in st:
            x += 1
            count += 1
        longest = max(count,longest)
print(longest)
