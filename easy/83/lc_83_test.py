from lc_83 import deleteDuplicates
from lc_83 import ListNode



def runTest():
    input = ListNode(val = 1, next = ListNode(val = 1, next = ListNode(val = 2, next = None)))
    expected = ListNode(val = 1, next = ListNode(val = 2, next = None))
    outputReturned = deleteDuplicates(input)
    
    
    
def runTest2():
    input =  ListNode(val = 1, next = ListNode(val = 1, next = ListNode(val = 2, next = ListNode(val = 3, next = ListNode(val = 3, next = None)))))
    expected = ListNode(val = 1, next = ListNode(val = 2, next = ListNode(val = 3, next = None)))
    outputReturned = deleteDuplicates(input)
    
def runTest3():
    input =  ListNode(val = 1, next = ListNode(val = 1, next = ListNode(val = 1, next = None)))
    expected = ListNode(val = 1, next = None)
    outputReturned = deleteDuplicates(input)
    
if __name__ == "__main__":
    runTest()
    runTest2()
    runTest3()