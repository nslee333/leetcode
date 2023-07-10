from lc_83 import deleteDuplicates
from lc_83 import ListNode

def runTest():
    input = ListNode(val = 1, next = ListNode(val = 1, next = ListNode(val = 2, next = None)))
    expected = ListNode(val = 1, next = ListNode(val = 2, next = None))
    outputReturned = deleteDuplicates(input)
    
    if outputReturned != expected:
        print(f"Ex. 1: error: outputReturned {outputReturned}, expected {expected}, input {input}")
        
def runTest2():
    input =  ListNode(val = 1, next = ListNode(val = 1, next = ListNode(val = 2, next = ListNode(val = 3, next = ListNode(val = 3, next = None)))))
    expected = ListNode(val = 1, next = ListNode(val = 2, next = ListNode(val = 3, next = None)))
    outputReturned = deleteDuplicates(input)
    
    if outputReturned != expected:
        print(f"Ex. 2: error: outputReturned {outputReturned}, expected {expected}, input {input}")

if __name__ == "__main__":
    runTest()
    runTest2()