##in this question we have to get maximum sub array  sum in a array 


##brute force soln 

def subarray_sum(arr):
    max=float("-inf")
    for i in range(0,len(arr)):
        total=0#reset fo each starting points
        for j in range(i,len(arr)):
            total+=arr[j]
            if total>=max:
                max=total
    return max   
print(subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))    


##optimmal soln:-kadane algorithm
def kadane(arr):
    current_sum=arr[0]
    maxi_sum=arr[0]
    for i in range(1,len(arr)):
        current_sum=max(arr[i],arr[i]+current_sum)
        maxi_sum=max(current_sum,maxi_sum)
    return maxi_sum
print(kadane([-2,1,-3,4,-1,2,1,-5,4]))    


