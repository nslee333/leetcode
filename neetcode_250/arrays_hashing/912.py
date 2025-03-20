# sort an array
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, L, M, R):
            left, right = arr[L:M + 1], arr[M + 1: R + 1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1

            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1
            
            
          

        def mergeSort(arr, l, r) -> List[int]:
            # this is bb
            if l == r:
                return

            mid = (l + r) // 2

            mergeSort(arr, l, mid)
            mergeSort(arr, mid + 1, r)
            merge(arr, l, mid, r)
            return

        mergeSort(nums, 0, len(nums))
        return nums




# ! Broken, not working, I explored a bit of why my code was wrong,
# I determined my time was best used learning the right way to do it.
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, L, M, R):
            res = []

            # this is wrong because left and right pointers at opposite ends, the problem is that if I have higher 
            # elements later, they won't be sorted, causing inaccuracy

            # the method is to split the array into two subarrays, and then use a left pointer 
            # on each, and then this structure below makes sense.
            while L < len(arr) and R < len(arr):
                if arr[L] <= arr[R]:
                    res.append(arr[L])
                elif arr[L] > arr[R]:
                    res.append(arr[R])

            while L < len(arr):
                res.append(arr[L])

            while R < len(arr):
                res.append(arr[R])

            return res
          

        def mergeSort(arr, l, r) -> List[int]:
            # this is bb
            if len(arr) <= 1:
                return arr

            mid = (l + r) // 2


            left = mergeSort(arr[l:mid], l, mid)
            right = mergeSort(arr[mid+1:r], mid + 1, r)

            return merge(left, l, mid, r) +  merge(right, l, mid, r)
        
        left, right = 0, len(nums) - 1
        return mergeSort(nums, left, right)




# merge sort solution
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0

            # merging while both are in range
            while j <  len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            
            # one or the other will be out of range, so this will fill out the remaining
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r) -> List[int]:
            if l == r:
                return arr

            
            m = (l + r) // 2
            # left half
            mergeSort(arr, l, m)
            # right half
            mergeSort(arr, m + 1, r)

            merge(arr, l, m, r)
            return arr

        return mergeSort(nums, 0, len(nums) - 1)