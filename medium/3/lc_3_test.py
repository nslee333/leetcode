from lc_3 import lengthOfLongestSubstring

def runTest():
    input = "abcabcbb"

    expected = 3

    output = lengthOfLongestSubstring(input)
    
    if output != expected:
        print(f"Ex. 1: error: output {output}, expected {expected}, input {input}")
        
def runTest2():
    input = "bbbbb"

    expected = 1

    output = lengthOfLongestSubstring(input)
    
    if output != expected:
        print(f"Ex. 2: error: output {output}, expected {expected}, input {input}")
        
def runTest3():
    input = "pwwkew"

    expected = 3

    output = lengthOfLongestSubstring(input)
    
    if output != expected:
        print(f"Ex. 2: error: output {output}, expected {expected}, input {input}")

if __name__ == "__main__":
    runTest()
    runTest2()
    runTest3()