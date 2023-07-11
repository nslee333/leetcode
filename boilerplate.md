from file import fn

def runTest():
    input = 0

    expected = 0

    output = fn(input)
    
    if output != expected:
        print(f"Ex. 1: error: output {output}, expected {expected}, input {input}")
        
def runTest2():
    input = 0

    expected = 0

    output = fn(input)
    
    if output != expected:
        print(f"Ex. 2: error: output {output}, expected {expected}, input {input}")
        
def runTest3():
    input = 0

    expected = 0

    output = fn(input)
    
    if output != expected:
        print(f"Ex. 2: error: output {output}, expected {expected}, input {input}")

if __name__ == "__main__":
    runTest()
    runTest2()
    runTest3()