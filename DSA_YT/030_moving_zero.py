#def zero_end(nums):
#    j=0
#    for i in range(len(nums)):

#        if nums[i]==0:
#            result=nums[i].remove()
#            result.insert(len(nums),nums[i])
#    return nums
#print(zero_end([89,0,67,75,32,0,9,0]))       


#### brute soln

# def zero_end(nums):
#     result=[]
#     temps=[]
#     for i in range(0,len(nums)):
#         if nums[i]!=0:
#             temps.append(nums[i])
#     for i in range(0,len(temps)):
#         nums[i]=temps[i]
#     for i in range(len(temps),len(nums)):
#         nums[i]=0
#     return nums
# print(zero_end([1,2,3,4,5,60,0,6,0,70,0,0,7]))


# optimal solnn
def zero_end(nums):
    if len(nums)==1:
        return
    i=0
    while i<len(nums):
        if nums[i]==0:
            break
        i+=1
    if i==len(nums):
        return
    j=i+1
    while j <(len(nums)):
            if nums[j]!=0:
                 nums[i],nums[j]=nums[j],nums[i]
                 i+=1
            j+=1     
    return nums
print(zero_end([1,2,3,4,5,60,0,6,0,70,0,0,7]))
             
            

                


        


               




