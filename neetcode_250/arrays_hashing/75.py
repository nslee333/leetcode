# sort colors, a sorting problem

# three pointer, 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1

# bucket sort, only possible because of limited numbers (0, 1, 2)
# linear runtime (but two pass)
# linear space
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = {x: 0 for x in range(3)}
       
        for item in nums:
            count[item] += 1

        i = 0
        for key in count.keys():
            while count[key] > 0:
                nums[i] = key
                count[key] -= 1
                i += 1








# my merge sort solution, loglinear runtime
# loglinear runtime, and linear space
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i,j,k = L, 0, 0

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
            

        def merge_sort(arr, l, r):
            if l == r:
                return

            m = (l + r) // 2

            merge_sort(arr, l, m)
            merge_sort(arr, m + 1, r)
            merge(arr, l, m, r)

            return arr
        
        merge_sort(nums, 0, len(nums))
        return nums

