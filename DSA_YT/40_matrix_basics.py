
# printing upper triangular matrix
def uppper_matrix(nums):
    rows=len(nums)
    cols=len(nums[0])
    for i in range(0,rows):
        for j in range(0,cols):
            if j>=i:
                print(nums[i][j],end=" ")
            else:
                print("*",end=" ")
        print()
print(uppper_matrix( [[1, 2, 3],[4, 5, 6],[7, 8, 9]]))                    

##printing lower triangular matrix

def uppper_matrix(nums):
    rows=len(nums)
    cols=len(nums[0])
    for i in range(0,rows):
        for j in range(0,cols):
            if i>=j:
                print(nums[i][j],end=" ")
            else:
                print("*",end=" ")
        print()
print(uppper_matrix( [[1, 2, 3],[4, 5, 6],[7, 8, 9]]))

# diagonal matix 
def uppper_matrix(nums):
    rows=len(nums)
    cols=len(nums[0])
    for i in range(0,rows):
        for j in range(0,cols):
            if i==j:
                print(nums[i][j],end=" ")
            else:
                print("*",end=" ")
        print()
print(uppper_matrix( [[1, 2, 3],[4, 5, 6],[7, 8, 9]]))

# reverse diagonal matrix.

def uppper_matrix(nums):
    rows=len(nums)
    cols=len(nums[0])
    for i in range(0,rows):
        for j in range(0,cols):
            if i+j==2:
                print(nums[i][j],end=" ")
            else:
                print("*",end=" ")
        print()
print(uppper_matrix( [[1, 2, 3],[4, 5, 6],[7, 8, 9]]))


def transpose(nums):
    rows=len(nums)
    cols=len(nums[0])
    result=[[0]*rows for _ in range (cols)]
    for i in range(0,rows):
        for j in  range(0,cols):
            result[j][i]=nums[i][j]
    return result        
print(transpose([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))

