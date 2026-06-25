###brute force soln

# def mark_infinity(nums,row,col):
#     r=len(nums)
#     c=len(nums[0])
#     for i in range(0,r):
#         if nums[i][col]!=0:
#             nums[i][col]=float("inf")

#     for j in range(0,c):
#         if nums[row][j]!=0:
#             nums[row][j]=float("inf")
# def serZeros(nums):
#     r=len(nums)
#     c=len(nums[0])
#     for i in range(0,r):
#         for j in range(0,c):
#             if nums[i][j]==0:
#                 mark_infinity(nums,i,j)
#     for i in range(0,r):
#         for j in range (0,c):
#             if nums[i][j]==float("inf"):
#                 nums[i][j]=0
#     return nums
# matrix=[[1, 0, 3],[4, 5, 6],[7, 8, 0]]

# print(serZeros(matrix))

####optimal solm

def zero_matrix(nums):
    r=len(nums)
    c=len(nums[0])
    rowTrack=[0 for _ in range(r)]
    colTrack =[0 for _ in range(c)]
    for i in range(0,r):
        for j in range(0,c):
            if nums[i][j]==0:
                rowTrack[i]=-1
                colTrack[j]=-1
    for i in range(0,r):
        for j in range(0,c):
            if rowTrack[i]==-1 or colTrack[j]== -1:
                nums[i][j]=0 
    return nums
print(zero_matrix([[1, 0, 3],[4, 5, 6],[7, 8, 0]]))

##TC==o(2*(n*m))
# sc =n*m           





