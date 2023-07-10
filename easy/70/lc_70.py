# 
# 
# You are climbing a staircase. It takes n steps to reach the top.
# 
# each time you can either climb 1 or 2 steps, in how many distinct ways can you climb to the top?
# 
# & This problem can be broken down into a fibonacci sequence


def climbStairs(n: int) -> int:
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
