import unittest


"""
Leetcode 49

Given an array of strings, group the anagrams together. You can return the answer in any order.

"""


class Solution:
    def group_anagrams(self, arr):
        result = []
        a = []
        for item in arr:
            x = "".join(sorted(item))
            a.append(x)
        a.sort()
        print(a)
        
        k = 0
        l = 1
        
        temp = []
        for i in range(len(a)):
            if l < len(a)-1 and k < len(a)-1:
                if a[k] == a[l]:
                    temp.append(a[k])
                    temp.append(a[l])
                
                k += 2
                l += 2
            result.append(temp)    
        print(result)
        return result



class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = ["eat","tea","tan","ate","nat","bat"]
        expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
        output = s.group_anagrams(input)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = [""]
        expected = [[""]]
        output = s.group_anagrams(input)
        
        self.assertEqual(output, expected)

    def test3(self):
        s = Solution()
        
        input = ["a"]
        expected = ["a"]
        output = s.group_anagrams(input)
        
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()