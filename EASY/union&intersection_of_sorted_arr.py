#  brute force approach
# arr1 = [1,1,3,4,5]
# arr2 = [3,4,4,5,6,2]
# s = set()
# for num in arr1:
#     s.add(num)
# for num in arr2:
#     s.add(num)
# s = sorted(s)
# print(list(s))
# optimal solution using two pointers
arr1 = [1,1,2,3,4,5]
arr2 = [3,4,4,5,6,]
i = 0
j = 0
union = []
while i<len(arr1) and j<len(arr2):
    if arr1[i]<=arr2[j]:
        if len(union) == 0 or union[-1]!=arr1[i]:
            union.append(arr1[i])
        i += 1
    else:
        if len(union) == 0 or union[-1]!=arr2[j]:
            union.append(arr2[j])
        j += 1
while i<len(arr1):
    if len(union) == 0 or union[-1]!=arr1[i]:
        union.append(arr1[i])
    i += 1
while j<len(arr2):
    if len(union) == 0 or union[-1]!= arr2[j]:
        union.append(arr2[j])
    j += 1
print(union) 