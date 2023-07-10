from lc_70 import climbStairs

def runTest():
    input = 2
    output = 2
    got = climbStairs(input)
    if got != output:
        print(f"Ex. 1: error: got {got}, output {output}, input {input}")
        
def runTest2():
    input = 3
    output = 3
    got = climbStairs(input)
    
    if got != output:
        print(f"Ex. 2: error: got {got}, output {output}, input {input}")
        
def runTest3():
    input = 8
    output = 21
    got = climbStairs(input)
    
    if got != output:
        print(f"Ex. 3: error: got {got}, output {output}, input {input}")
        
def runTest4():
    input = 10
    output = 55
    got = climbStairs(input)
    
    if got != output:
        print(f"Ex. 3: error: got {got}, output {output}, input {input}")
        
if __name__ == "__main__":
    runTest()
    runTest2()
    runTest3()
    runTest4()