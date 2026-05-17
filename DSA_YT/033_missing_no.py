# ##in this problem we have to find missing number in a list from the length of list
# 
# #brute force solm
#  
# def missing_num(nums):
#     n=len(nums)
#     # nums.sort()
#     for i in range(0,n+1):
#         if i not in (nums):
#             return i        
# print(missing_num([0,1,2,4,5,3]))

##better soln

# def missing_nums(nums):
#     n=len(nums)
#     freq={}
#     for i in range(0,n+1):
#         freq[i]=0
#     for num in nums:
#         freq[num]=1
#     for k,v in freq.items():
#         if v==0:
            # return k
               
##optimal solution
def missing_num(nums):
    n=len(nums)
    return n*(n+1)/2-sum(nums)
print(missing_num([0,1,2,4,5,3]))


