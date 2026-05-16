# findig first occurence of target element in array by iterating element one by one is called as linear search


def linear_search(arr,targ):

    for i in range(0,len(arr)):
        if arr[i]==targ:
            return i
    

    return -1        
targ=int(input("enter the element you wanna search: "))
print(linear_search([1,2,3,44,5,5,4,34,5,4,5,4],targ))


    