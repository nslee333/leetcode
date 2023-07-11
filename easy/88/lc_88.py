from typing import List

# 
# ! merge two integer arrays together sorted in a non-decreasing order.
# 
# 

def merge_arrs(arr1, arr2):
    result = []
    
    for i, j in arr1, arr2:

        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
            
        else:
            result.append(arr2[j])
            j += 1
            
        # & Need to handle remaining elements here -> 
    return result


def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    left = 0
    right = len(arr)-1
    
    if len(arr) >= 2:
        middle = len(list) / 2
        
    merge_sort(arr[:middle], arr[middle:])
    
    



def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1 = nums1[:m]
    nums2 = nums2[:n]
    
    for item in nums2:
        nums1.append(item)
    
    # TODO need to chang the sig of merge_sort()
    nums1 = merge_arrs(merge_sort())
    