import unittest

"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 

Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. 

The richest customer is the customer that has the maximum wealth.
"""

class Solution:
    # O(N squared) time complexity because I have nested loops.
    def maximumWealth(self, accounts):
        highest_total = 0 
        
        for acc in accounts:
            sum = 0
            
            for bal in acc:
                sum += bal
                
            if sum > highest_total:
                highest_total = sum

        return highest_total
    

        
class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        
        input = [[1,2,3],[3,2,1]]
        expected = 6
        output = s.maximumWealth(input)
        
        self.assertEqual(output, expected)
                
    def test2(self):
        s = Solution()
        
        input = [[1,5],[7,3],[3,5]]
        expected = 10
        output = s.maximumWealth(input)
        
        self.assertEqual(output, expected)
        
    def test3(self):
        s = Solution()
        
        input = [[2,8,7],[7,1,3],[1,9,5]]
        expected = 17
        output = s.maximumWealth(input)
        
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
