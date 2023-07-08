from lc_69 import mySqrt

def runTest():
    input_x = 4
    output = 2
    got = mySqrt(input_x)
    
    if got != output:
        print(f"Ex. 1: error: got {got}, output {output}, input_x {input_x}")
        
def runTest():
    input_x = 8
    output = 2
    got = mySqrt(input_x)
    
    if got != output:
        print(f"Ex. 2: error: got {got}, output {output}, input_x {input_x}")
        
if __name__ == "__main__":
    runTest()