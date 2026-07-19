# given row and col number tell the element at that place
# r = int(input())
# c = int(input())
# def ncr(n,r):
#     res = 1
#     for i in range(r):
#         res *= n-i
#         res //= i+1
#     return res
# print(ncr(r-1,c-1))  
# print any nth row of pascals triangle
# brute force solution
# row = int(input())
# def ncr(n,r):
#     res = 1
#     for i in range(r):
#         res *= n-i
#         res //= i+1
#     return res
# for i in range(1,row+1):
#     print(ncr(row-1,i-1),end=" ")
# print any nth row of pascals triangle optimal solution 
# row = int(input())
# ans = 1
# print(ans,end=" ")
# for i in range(1,row+1):
#     ans *= row - i
#     ans //= i
#     print(ans,end=" ")
# # print pascal triangle brute force solution
# n = int(input())
# ans = []
# def ncr(n,r):
#     res = 1
#     for i in range(r):
#         res *= n-i
#         res //= i+1
#     return res
# for i in range(1,n+1):
#     temp = []
#     for j in range(1,i+1):
#         temp.append(ncr(i-1,j-1))
#     ans.append(temp)        
# for i in ans:
#     print(i,end=" ")
# better solution solution 
n = int(input())
for k in range(1,n+1):
    ans = 1
    print(ans,end=" ")
    for i in range(1,k):
        ans = ans*(k-i)
        ans = ans//(i)
        print(ans,end=" ")
    print()


