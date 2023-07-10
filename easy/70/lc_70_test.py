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

if __name__ == "__main__":
    runTest()
    runTest2()