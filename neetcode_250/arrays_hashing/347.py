# top k freq elements

# bucket sort algorithm, linear time and space

# it sorts it by setting up freq buckets, and putting the count as the index.
# corresponding [freq count] = number

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # n possible buckets

        # count frequency
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # swap element and count
        for n, c in count.items():
            freq[c].append(n)

        res = []

        for bucket in range(len(freq) - 1, 0, -1):
            for n in freq[bucket]:
                res.append(n)
                if len(res) == k:
                    return res

# my solution
# O(n + (n log n) + k) so not great performance wise
# linear space since we need table (N elements) & res array of K elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # worst case in linear space
        table = {}

        # linear runtime cost
        for item in nums:
            table[item] = 1 + table.get(item, 0)
        
        # loglinear runtime cost
        temp = sorted(table.items(), key=lambda item: item[1], reverse=True)

        # K space
        res = []

        # K runtime cost
        for item in range(k):
            res.append(temp[item][0])

        return res
