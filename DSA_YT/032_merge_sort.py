def merge_sort(nums1,nums2):
    i=0
    j=0
    result=[]
    while i<len(nums1) and j < len(nums2):
        if nums1[i]==nums2[j]:
            if len(result)==0 or result[-1]!=nums1[i]:
                result.append(nums1[i])
            i+=1
        else:
            if len(result)==0 or result[-1]!=nums2[j]:
                result.append(nums2[j])
            j+=1
    return result
print(merge_sort([1,3,2,34,53],[1,34,34,5,33,43,4,3,43]))            
                    