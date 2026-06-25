##to get profit from max 
# brute force soln
def stock(arr):
    arr=[1,2,34,5,3,53,345,3,3,4,3,3,45,43]
    max_profits=0
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                p=arr[j]-arr[i]
                max_profits=max(p,max_profits)
    return max_profits
            
print(stock([1,2,34,5,3,53,345,3,3,4,3,3,45,43]))

#optimal soln

def stock_profit(arr):
    # buy=0
    max_profit=0
    min_price=float("inf")
    for i in range(0,len(arr)):
        min_price=min(min_price,arr[i])
        if arr[i]>min_price:
            max_profit=max(arr[i]-min_price,max_profit)
    return max_profit

print(stock_profit([1,2,34,5,3,53,345,3,3,4,3,3,45,43]))  
