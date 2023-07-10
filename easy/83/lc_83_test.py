from lc_83 import deleteDuplicates

def runTest():
    input = 2
    expected = 2
    outputReturned = deleteDuplicates(input)
    if outputReturned != expected:
        print(f"Ex. 1: error: outputReturned {outputReturned}, expected {expected}, input {input}")
        
def runTest2():
    input = 3
    expected = 3
    outputReturned = deleteDuplicates(input)
    
    if outputReturned != expected:
        print(f"Ex. 2: error: outputReturned {outputReturned}, expected {expected}, input {input}")

if __name__ == "__main__":
    runTest()
    runTest2()