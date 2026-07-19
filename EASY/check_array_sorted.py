arr = [1,2,2,3,4]
sorted_flag = True
for i in range(1,len(arr)):
    if arr[i]>=arr[i-1]:
        pass
    else:
        sorted_flag = False
        break
if sorted_flag:
    print("sorted")
else:
    print("not sorted")