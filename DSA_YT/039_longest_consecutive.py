
#brute force soln

# def longest_consective(nums):
#     max_count=0
#     for i in range(0,len(nums)):
#         num =nums[i]
#         count=1
#         while num+1 in nums:
#             count+=1
#             num +=1
#         max_count=max(max_count,count)
#     return max_count
# print(longest_consective([1,99,101,98,2,5,3,100,1,1]))        

#better soln
def long_consecutive(nums):
    nums.sort()
    last_smaller=float("-inf")
    count=0
    longest=0
    for i in range(0,len(nums)):
        if (nums[i]-last_smaller)!=1:
            count=1

            last_smaller=nums[i]
        # if (nums[i]-last_smaller)==1:
        else:
            count+=1
        longest=max(longest,count)
            
        last_smaller=nums[i]
    return longest        
print(long_consecutive([1,99,101,98,2,5,3,100,1,1,1,1]))

            



# optimal soln: using set

def longest_consec(nums):
    my_set=set()
    for i in range(0,len(nums)):
        my_set.add(nums[i])
    longest=0
    for num in my_set:
        if (num-1) not in my_set:
            current_num=num
            count=1
            while current_num+1 in my_set:
                count+=1
                current_num+=1
            longest=max(longest,count)
    return longest
print(longest_consec([1,99,101,98,2,5,3,100,1,1,1,1]))




    





