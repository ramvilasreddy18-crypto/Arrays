arr = [7,1,5,3,6,4] # arr represents stock price on ith day
n = len(arr)
mini = arr[0]
profit = 0 # profit should not be negative so we assinged 0
for i in range(1,n): #we start loop from 1 becase it is selling we cant sell 0th index becase we have rule we cant sell and buy on same day
    cost = arr[i] - mini # selling stock
    profit = max(profit,cost)
    mini = min(mini,arr[i]) # update the mini
print(profit)
