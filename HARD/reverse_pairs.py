# brute force soln
nums = [40, 25, 19, 12, 9, 6, 2]
count = 0
n = len(nums)
for i in range(n-1):
    for j in range(i+1,n):
        if nums[i]>nums[j]*2:
            count += 1
print(count)
# optimal solution
def reversePairs(nums):
    def merge(arr, low, mid, high):
        count = 0
        right = mid + 1

        for i in range(low, mid + 1):
            while right <= high and arr[i] > 2 * arr[right]:
                right += 1
            count += right - (mid + 1)

        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]

        return count

    def merge_sort(arr, low, high):
        if low >= high:
            return 0

        mid = (low + high) // 2

        count = merge_sort(arr, low, mid)
        count += merge_sort(arr, mid + 1, high)
        count += merge(arr, low, mid, high)

        return count

    return merge_sort(nums, 0, len(nums) - 1)


nums = [40, 25, 19, 12, 9, 6, 2]
print(reversePairs(nums))