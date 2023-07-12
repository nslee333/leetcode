from lc_4 import findMedianSortedArrays

def runTest():
    nums1 = [1,3]
    nums2 = [2]

    expected = 2.00000

    output = findMedianSortedArrays(nums1, nums2)
    
    if output != expected:
        print(f"Ex. 1: error: output {output}, expected {expected}, nums1 {nums1}, nums2 {nums2}")
        
def runTest2():
    nums1 = [1,2]
    nums2 = [3,4]

    expected = 2.50000

    output = findMedianSortedArrays(nums1, nums2)
    
    if output != expected:
        print(f"Ex. 2: error: output {output}, expected {expected}, nums1 {nums1}, nums2 {nums2}")
        
def runTest3():
    nums1 = []
    nums2 = []

    expected = 0

    output = findMedianSortedArrays(nums1, nums2)
    
    if output != expected:
        print(f"Ex. 2: error: output {output}, expected {expected}, nums1 {nums1}, nums2 {nums2}")

if __name__ == "__main__":
    runTest()
    runTest2()
    # runTest3()