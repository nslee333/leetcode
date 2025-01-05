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