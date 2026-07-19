# brute force approach
# arr = [2,6,5,8,11]
# target = 14
# flag = False
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]+arr[j] == target:
#             print(i,j)
#             flag = True
# if flag == False:
#     print("not found ")
# optimal solution using hashing
arr = [2,6,5,8,11]
target = 14
mpp = {}
for i in range(len(arr)):
    more_needed = target - arr[i]
    if more_needed in mpp:
        print(i,mpp[more_needed])
        break
    mpp[arr[i]] = i
# better for saying yes or no means sum present or not 
arr = [2,6,5,8,11]
target = 14
arr.sort()
left = 0
right = len(arr)-1
while(left<right):
    tot = arr[left] + arr[right]
    if tot>target:
        right -= 1
    if tot < target:
        left += 1
    if tot == target:
        print("yes")
        break


