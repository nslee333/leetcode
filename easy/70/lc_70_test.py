from lc_70 import climbStairs

def runTest():
    input = 2
    output = 2
    got = climbStairs(input)
    
    if got != output:
        print(f"Ex. 1: error: got {got}, output {output}, input {input}")
        
def runTest():
    input = 3
    output = 3
    got = climbStairs(input)
    
    if got != output:
        print(f"Ex. 2: error: got {got}, output {output}, input {input}")
        
if __name__ == "__main__":
    runTest()