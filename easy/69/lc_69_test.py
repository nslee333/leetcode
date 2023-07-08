from lc_69 import mySqrt

def runTest():
    input_x = 4
    output = 2
    got = mySqrt(input_x)
    
    if got != output:
        print(f"error: got {got}, output {output}, input_x {input_x}")
        
if __name__ == "__main__":
    runTest()