arr = [3,1,-2,-5,2,4]
pos = []
neg = []
for nums in arr:
    if nums>0:
        pos.append(nums)
    else:
        neg.append(nums)
if len(pos)>len(neg):
    for i in range(len(neg)):
        arr[2*i] = pos[i]
        arr[2*i+1] = neg[i]
    index = len(neg)*2
    for i in range(len(neg),len(pos)):
        arr[index] = pos[i]
        index += 1 
else:
    for i in range(len(pos)):
        arr[2*i] = pos[i]
        arr[2*i+1] = neg[i]
    index = len(pos)*2
    for i in range(len(pos),len(neg)):
        arr[index] = neg[i]
        index += 1 
print(arr)
