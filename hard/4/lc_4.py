from typing import List

"""
given two sorted arrays return the median of the two sorted arrays

the overall runtime complexity should be o(log (m+n))

we need to merge the two arrays then find the median -> two middle elements / 2

"""

def merge_sort(arr1, arr2):
    merged = []
    i, j = 0,0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
            
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
        
    return merged
    
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    merged = merge_sort(nums1, nums2)
    result = 0.0
    
    if len(merged) % 2 != 0:
        location = len(merged) // 2
        result = merged[location]
        
    else:
        mergeLen = len(merged)
        first = mergeLen // 2
        sec = first - 1 
        result = (merged[first] + merged[sec]) / 2
        
    return result
    