class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # loop through array

        table = {}

        # O N
        for item in nums:
            if table.get(item):
                table[item] += 1
            else: 
                table[item] = 1

        # n log n -> O N
        result = dict(sorted(table.items()))
        print(result)

        result2 = []

        # o N
        for key, value in result.items():
            print(k, len(result))
            if len(result2) == k:
                return result2
            result2.append(key)
# this isn't solved yet


# neetcode
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # loop through array

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

# my modified solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # loop through array

        # we need to 
        count = {}

        freq = [[] for i in range(len(nums) + 1)]
        
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        print(freq)

        for num, cnt in count.items():
            freq[cnt].append(num)
            

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
