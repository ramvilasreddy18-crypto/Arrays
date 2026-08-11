# brute force solution
arr = [4,3,6,2,1,1]
n = len(arr)
missing = -1
repeating = -1
for i in range(1,n):
    count = 0
    for j in range(n):
        if arr[j] == i:
            count += 1
    if count == 2:
        repeating = i
    elif count == 0:
        missing = i
    if repeating != -1 and missing != -1:
        break
print({missing,repeating})
# better solution using hashing
arr = [4,3,6,2,1,1]
n = len(arr)
missing = -1
repeating = -1
hash = [0]*(n+1)
for i in arr:
    hash[i] += 1
for i in range(1,n+1):
    if hash[i] == 2:
        missing = i
    elif hash[i] == 0:
        repeating = i
    if repeating != -1 and missing != -1:
        break
print({repeating,missing})
# optimal using basic maths 
arr = [4,3,6,2,1,1]
n = len(arr)
s = s2 = 0 # s = sum of nums in array s2 = squares of nums in arr
for num in arr:
    s += num
    s2 += num * num
sn = (n * (n+1))//2 # sn = sum of natural nums from 1 to n 
s2n = (n*(n+1)*(2*n+1))//6 # s2n = sum of squares of natural nums from 1 to n
val1 = s-sn # x - y = val1
val2 = s2 - s2n # x^2 - y^2 = val2
val2 = val2 // val1 # val2 = x+y
x = (val1+val2)//2
y = val2 - x
print({x,y})
# optimal solution using xor
def findMissingRepeatingNumbers(arr):
    n = len(arr)

    xr = 0

    for i in range(n):
        xr ^= arr[i]
        xr ^= i + 1

    bit = 0
    while True:
        if xr & (1 << bit):
            break
        bit += 1

    zero = 0
    one = 0

    for num in arr:
        if num & (1 << bit):
            one ^= num
        else:
            zero ^= num

    for i in range(1, n + 1):
        if i & (1 << bit):
            one ^= i
        else:
            zero ^= i

    if arr.count(zero) == 2:
        return [zero, one]
    return [one, zero]

