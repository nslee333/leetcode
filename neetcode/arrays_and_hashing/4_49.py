
# Came up with this idea fairly quickly
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}

        for i in range(len(strs)):
            item = ''.join(sorted(strs[i]))
            if hash_table.get(item) == None:
                hash_table[item] = [strs[i]]
            elif hash_table.get(item) != None:
                hash_table[item].append(strs[i])
        
        result = []

        for arr in hash_table.values():
            result.append(arr)
        return sorted(result)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        hash_table = defaultdict(list)

        for s in strs:
            char_count = [0] * 26
            
            for c in s:
                char_count[ord(c) - ord('a')] += 1

            hash_table[tuple(char_count)].append(s)
        return list(hash_table.values())
