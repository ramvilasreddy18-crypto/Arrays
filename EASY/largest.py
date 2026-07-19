n = int(input("enter no of ele in array : "))
arr = [0]*n
for i in range(n):
    arr[i] = int(input("enter ele : "))
largest = arr[0]
for i in range(n):
    if largest<arr[i]:
        largest = arr[i]
print(largest)