# #Brute force approach
# arr = [1,2,3,4,5,6,7]
# d = int(input("enter no spaces to shift left side : "))
# n = len(arr)
# d = d % n
# temp = [None]*d
# print(arr)
# # store first d ele in temp
# for i in range(d):
#     temp[i] = arr[i]
# # shift ele towards d left 
# for i in range(d,n):
#     arr[i-d] = arr[i]
# # put back stored ele in array from temp
# j = 0 
# for i in range(n-d,n):
#     arr[i] = temp[j]
#     j += 1
# print(arr)
#optimal solution
arr = [1,2,3,4,5,6,7]
d = int(input("enter no spaces to shift left side : "))
n = len(arr)
d = d % n
def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
reverse(arr,0,d-1)
reverse(arr,d,n-1)
reverse(arr,0,n-1)
print(arr)