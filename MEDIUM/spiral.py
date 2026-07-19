n,m = map(int,(input().split()))
arr = []
for _ in range(n):
    row = list(map(int,input().split()))
    arr.append(row)
top = 0
bottom = n-1
left = 0
right = m-1
ans = []
while(top<=bottom and left<=right):
    # right
    for i in range(left,right+1):
        ans.append(arr[top][i])
    top += 1
    # bottom 
    for i in range(top,bottom+1):
        ans.append(arr[i][right])
    right -= 1
    # left
    if top<=bottom:
        for i in range(right,left-1,-1):
            ans.append(arr[bottom][i])
        bottom -= 1
    # top
    if left<=right:
        for i in range(bottom,top-1,-1):
            ans.append(arr[i][left])
        left += 1
print(*ans)
    
    