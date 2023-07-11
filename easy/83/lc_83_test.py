from lc_83 import deleteDuplicates
from lc_83 import ListNode



def printVals(head: ListNode, num: int):
    for elem in range(num):
        print(head.val)
        if head.next == ListNode: head = head.next
        if head.next == None: break




def runTest():
    input = ListNode(val = 1, next = ListNode(val = 1, next = ListNode(val = 2, next = None)))
    expected = ListNode(val = 1, next = ListNode(val = 2, next = None))
    outputReturned = deleteDuplicates(input)
    

    print("expected")
    printVals(expected, 2)
    print("returned")
    printVals(outputReturned, 3)
        
def runTest2():
    input =  ListNode(val = 1, next = ListNode(val = 1, next = ListNode(val = 2, next = ListNode(val = 3, next = ListNode(val = 3, next = None)))))
    expected = ListNode(val = 1, next = ListNode(val = 2, next = ListNode(val = 3, next = None)))
    outputReturned = deleteDuplicates(input)
    
    
    print("expected")
    printVals(expected, 3)
    print("returned")
    printVals(outputReturned, 3)

if __name__ == "__main__":
    runTest()
    runTest2()