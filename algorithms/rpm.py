"""
This is an implementation of the russian peasant multiplcation algoritm.

"""
import math
import pandas as pd


def rpm(n1, n2):
    halving = [n1]
    while(min(halving) > 0):
        halving.append(math.floor(min(halving)/2))

    doubling = [n2]
    
    while(len(doubling) < len(halving)):
        doubling.append(max(doubling)*2)


    print(halving)
    print(doubling)
    half_double = pd.DataFrame(zip(halving,doubling))
if __name__ == "__main__":
    rpm(89, 18)