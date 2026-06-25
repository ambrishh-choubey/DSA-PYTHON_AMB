##in this problem we hAVE arrange number in a list based on alternate sign 

# brute forcessoln
def rearrange(nums):
    pos=[]
    neg=[]
    for num in nums:
        if num>=0:
            pos.append(num)
        else:
            neg.append(num)
    for i in range(0,len(pos)):
        nums[2*i]=pos[i]
    for j in range(0,len(neg)):
        nums[2*j+1]=neg[j]
                
    return nums
print(rearrange([5,10,-3,-1,-10,6]))

#optimal_soln

def rearrange_sign(nums):
    p=0
    n=1
    result=[0]*len(nums)
    for i in range (0,len(nums)):
        if nums[i]>=0:
            result[p]=nums[i]
            p+=2
        else:
            result[n]=nums[i]
            n+=2
    return result
print(rearrange_sign([5,10,-3,-1,-10,6]))            






