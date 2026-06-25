####solving by making diferent variable result

# def rotate_matrix(nums):
#     r=len(nums)
#     c=len(nums[0])
#     result=[[0 for _ in range(r)] for _ in range(r)]
#     for i in range(0,r):
#         for j in range(0,c):
#             result[j][r-1-i]=nums[i][j]
#     return result
# print(rotate_matrix([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]))  

def rotateMatrix(nums):
    r= len(nums)
    c=len(nums[0])
    for i in  range(0,r):
        for j in range(i+1,r):
            nums[i][j],nums[j][i]=nums[j][i],nums[i][j]
    for i in range(0,r):
        nums[i].reverse()
    return nums
print(rotateMatrix([[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]
 ]))  



