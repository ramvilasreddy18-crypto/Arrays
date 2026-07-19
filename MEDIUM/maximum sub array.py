# BRUTE FORCE APPROACH (TIME COMPLXITY IS O(n^3))
arr = [-2,-3,4,-1,-2,1,5,-3]
n = len(arr)
maxi = float('-inf')
for i in range(n):
    for j in range(i,n):
        tot = 0
        for k in range(i,j+1):
            tot += arr[k]
            maxi = max(tot,maxi)
print(maxi) 
# BETTER SOLUTION 
arr = [-2,-3,4,-1,-2,1,5,-3]
n = len(arr)
maxi = float('-inf')
for i in range(n):
    tot = 0
    for j in range(i,n): 
        tot += arr[j]
        maxi = max(tot,maxi)
print(maxi) 
# OPTIMAL SOLUTION (KADANES ALGORITHM)
arr = [-2,-3,4,-1,-2,1,5,-3]
n = len(arr)
tot = 0
maxi = float('-inf')
for i in range(n):
    tot += arr[i]
    if tot<0:
        tot = 0
    if tot>maxi:
        maxi = tot
if maxi<0: #THIS CONDITION IS BECAUSE IF ARRAY CONTAINS ONLY NEGATIVE VALUES THEN THE ANSWER SHOULD BE EMPTY SET
    print(0)
else: 
    print(maxi)
# IF WE WANT TO PRINT ARRAY ALSO 
arr = [-2,-3,4,-1,-2,1,5,-3]
n = len(arr)
tot = 0
num = []
maxi = float('-inf')
for i in range(n):
    if tot == 0:
        start = i
    tot += arr[i]
    if tot>maxi:
        maxi = tot
        ansstart = start
        ansend = i
    if tot<0:
        tot = 0
if maxi<0: #THIS CONDITION IS BECAUSE IF ARRAY CONTAINS ONLY NEGATIVE VALUES THEN THE ANSWER SHOULD BE EMPTY SET
    print(0)
else: 
    print(maxi)
for i in range(ansstart,ansend+1):
    ele = arr[i]
    num.append(ele)
print(num)

