from lc_83 import deleteDuplicates

def runTest():
    input = [1,1,2]
    expected = [1,2]
    outputReturned = deleteDuplicates(input)
    
    if outputReturned != expected:
        print(f"Ex. 1: error: outputReturned {outputReturned}, expected {expected}, input {input}")
        
def runTest2():
    input = [1,1,2,3,3]
    expected = [1,2,3]
    outputReturned = deleteDuplicates(input)
    
    if outputReturned != expected:
        print(f"Ex. 2: error: outputReturned {outputReturned}, expected {expected}, input {input}")

if __name__ == "__main__":
    runTest()
    runTest2()