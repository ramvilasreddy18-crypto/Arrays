arr = [1,2,4,2,1,4,5,6,4,63,6,72,4]
num = int(input("enter num to search : "))
found = False
for i in range(len(arr)):
    if arr[i] == num:
        print(i)
    found = True
if found:
    print("not found")
    