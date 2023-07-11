from lc_2 import addTwoNumbers, ListNode, convertLLtoArr

def runTest():
    l1 = ListNode(val = 2, next = ListNode(val = 4, next = ListNode(val = 3, next = None)))
    l2 = ListNode(val = 5, next = ListNode(val = 6, next = ListNode(val = 4, next = None)))
    
    expected = [7, 0, 8]
    
    outputReturned = addTwoNumbers(l1, l2)
    outputConverted = convertLLtoArr(outputReturned)
    
    print(f"Ex. 1: outputConverted {outputConverted}, expected {expected}")
        
def runTest2():
    l1 = ListNode(val = 0, next = None)
    l2 = ListNode(val = 0, next = None)
    expected = [0]
    
    outputReturned = addTwoNumbers(l1, l2)
    outputConverted = convertLLtoArr(outputReturned)
    
    print(f"Ex. 2: outputConverted {outputConverted}, expected {expected}")
        
def runTest3():
    l1 = ListNode(
        val = 9, next = ListNode(
            val = 9, next = ListNode(
                val = 9, next = ListNode(
                    val = 9, next = ListNode(
                        val = 9, next = ListNode(
                            val = 9, next = ListNode(
                                val = 9, next = None
                            )
                        )
                    )
                )
            )
        )
    )
    
    l2 = ListNode(val = 9, next = ListNode(val = 9, next = ListNode(val = 9, next = ListNode(val = 9, next = None))))

    l1converted = convertLLtoArr(l1)
    l2converted = convertLLtoArr(l2)
    
    expected = [8,9,9,9,0,0,0,1]
    
    outputReturned = addTwoNumbers(l1, l2)
    outputConverted = convertLLtoArr(outputReturned)
    
    
    print(f"Ex. 2: outputConverted {outputConverted}, expected {expected}")
    print(f"Ex. 2: l1converted {l1converted}, l2converted {l2converted}")

if __name__ == "__main__":
    # runTest()
    # runTest2()
    runTest3()