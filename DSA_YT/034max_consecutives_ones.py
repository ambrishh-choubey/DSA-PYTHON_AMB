#### in a list containing 0 and 1 only find the consecutives number of 0 and 1

def consecutive_ones(nums):
    count=0
    max_count=0
    for i in range(0,len(nums)):
        if nums[i]==1:
            count+=1
            if max_count < count:
                max_count=count
        else:
            count=0
    return max_count
print(consecutive_ones([0,1,2,3,1,1,1,2,1,1,21,1,11,1,]))        
