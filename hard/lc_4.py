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


# & Another solution, although this solution uses Python's builtin sort() 
# & which is probably frowned upon for an interview.

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         sorted_arr = nums1 + nums2
#         sorted_arr.sort()

#         if len(sorted_arr) % 2 == 0:
#             a = (len(sorted_arr) - 1) // 2
#             b = a + 1
#             return (sorted_arr[a] + sorted_arr[b]) / 2
#         else:
#             index = (len(sorted_arr) - 1) // 2
#             return sorted_arr[index]

# & Neetcode solution, this one doesn't combine both arrays

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         A, B = nums1, nums2
#         total = len(nums1) + len(nums2)
#         half = total // 2

#         if len(B) < len(A):
#             A, B = B, A
        
#         l, r = 0, len(A) - 1
#         while True:
#             i = (l + r) // 2
#             j = half - i - 2 

#             Aleft = A[i] if i >= 0 else float("-infinity")
#             Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
#             Bleft = B[j] if j >= 0 else float("-infinity")
#             Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

#             if Aleft <= Bright and Bleft <= Aright:
#                 if total % 2:
#                     return min(Aright, Bright)
#                 return(max(Aleft, Bleft) + min(Aright, Bright)) / 2
#             elif Aleft > Bright:
#                 r = i - 1
#             else:
#                 l = i + 1