##finding the sum of teo nums in a list so that sum is equal to target

#brute force solutiion


def two_sums(nums,target):
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if i==j:
                continue
            else:
                if nums[i]+nums[j]==target:
                    return i,j
print(two_sums([1,2,34,5,4,5,4,5,4,5,4,54,4,5,4,5,4,4,4,4],9)) 


# optimal__soln.......................
def two_sums(nums,target):
    hash_map=dict()
    remaining=0
    for i in range(0,len(nums)):

        remaining=target-nums[i]
        if remaining in hash_map:
            return (hash_map[remaining],i)
        hash_map[nums[i]]=i
print(two_sums([1,2,34,5,4,5,4,5,4,5,4,54,4,5,4,5,4,4,4,4],9)) 



