# arr = [1,1,2,2,2,2,3,3,3] brute force approach
# unique = list(set(arr))
# print(unique)
#  arr = [1,1,2,2,2,3,3] brute force simlarly

# s = set()

# for num in arr:
#     s.add(num)

# index = 0

# for num in s:
#     arr[index] = num
#     index += 1
#optimal with 2 pointers
arr = [1,1,2,2,3,3,4,5]
i = 0
for j in range(1,len(arr)):
    if arr[j]!=arr[i]:
        arr[i+1] = arr[j]
        i += 1
print(arr)
print(i+1) # here we are just puting the unique ele forward and return no of unique elements in the array 