##### we have to  print the matix in spiral way like hoe the spring work#####\

###soln

def spiral_matrix(nums):
    n=len(nums)

    top=0
    left=0
    bottom=n-1
    right=len(nums[0])-1
    while top <= bottom and left <=right:
        #left to right

        for i in range(left,right+1):
            print(nums[top][i],end=" ")
        top+=1

        # top to bottom
        for i in range(top,bottom+1):
            print(nums[i][right],end =" ")
        right-=1

        # right to left
        if top <= bottom:
            for i in range(right,left-1,-1):
                print(nums[bottom][i],end=" ")
            bottom-=1  

            # bottom to top
        if left<=right:
            for i in range(bottom,top-1,-1):
                print(nums[i][left],end=" ")
            left+=1     
            
print(spiral_matrix([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
]))

  