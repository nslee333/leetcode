from lc_70 import climbStairs

def runTest():
    input = 2
    expected = 2
    outputReturned = climbStairs(input)
    if outputReturned != expected:
        print(f"Ex. 1: error: outputReturned {outputReturned}, expected {expected}, input {input}")
        
def runTest2():
    input = 3
    expected = 3
    outputReturned = climbStairs(input)
    
    if outputReturned != expected:
        print(f"Ex. 2: error: outputReturned {outputReturned}, expected {expected}, input {input}")
        
def runTest3():
    input = 8
    expected = 21
    outputReturned = climbStairs(input)
    
    if outputReturned != expected:
        print(f"Ex. 3: error: outputReturned {outputReturned}, expected {expected}, input {input}")
        
def runTest4():
    input = 10
    expected = 55
    outputReturned = climbStairs(input)
    
    if outputReturned != expected:
        print(f"Ex. 4: error: outputReturned {outputReturned}, expected {expected}, input {input}")
        
if __name__ == "__main__":
    runTest()
    runTest2()
    runTest3()
    runTest4()