# brute force approach
# n = int(input())
# nums = list(map(int,input().split()))
# def duplicate(nums):
#     for i in range(n):
#         for j in range(i+1,n):
#             if nums[i] == nums[j]:
#                 return True
#     return False
# print(duplicate(nums))
# better solution
# n = int(input())
# nums = list(map(int,input().split()))
# def duplicate(nums):
#     mpp = {}
#     for num in nums:
#         mpp[num] = mpp.get(num,0)+1
#     for key,value in mpp.items():
#         if value>1:
#             return True
#     return False
# print(duplicate(nums))
# optimal solution 
# n = int(input())
# nums = list(map(int,input().split()))
# def duplicate(nums):
#     nums.sort()
#     for i in range(1,n):
#         if nums[i-1] == nums[i]:
#             return True
#     return False
# print(duplicate(nums))
# most optimal solution
seen = set()
n = int(input())
nums = list(map(int,input().split()))
def duplicate(nums):
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
print(duplicate(nums))

