from lc_88 import merge

def runTest():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    expected = [1,2,2,3,5,6]
    outputReturned = merge(nums1, m, nums2, n)
    if outputReturned != expected:
        print(f"Ex. 1: error: outputReturned {outputReturned}, expected {expected}, nums1 {nums1} m {m} nums2 {nums2} n {n}")
        
def runTest2():
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    expected = [1]
    outputReturned = merge(nums1, m, nums2, n)
    
    if outputReturned != expected:
        print(f"Ex. 2: error: outputReturned {outputReturned}, expected {expected}, nums1 {nums1} m {m} nums2 {nums2} n {n}")
        
def runTest3():
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    expected = [1]
    outputReturned = merge(nums1, m, nums2, n)
    
    if outputReturned != expected:
        print(f"Ex. 2: error: outputReturned {outputReturned}, expected {expected}, nums1 {nums1} m {m} nums2 {nums2} n {n}")

if __name__ == "__main__":
    runTest()
    runTest2()
    runTest3()