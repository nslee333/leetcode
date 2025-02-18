

# neetcode solution, O(N log N) time, O(N) space
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [[p,s] for p,s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)



# broken code, right idea, poor execution
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        hash = {}

        for i in range(len(position)):
            hash[position[i]] = speed[i]

        sorted_hash = {k: hash[k] for k in sorted(hash)}

        days = []

        for pos,speed in sorted_hash.items():
            day = (target - pos) / speed
            days.append(day)

        stack = []
        res = 0


        print(days)
        for r in range(len(days) - 1, 0, -1):

            if not stack:
                stack.append(days[r])

            elif days[r] <= stack[-1] or r == 0:
                stack.append(days[r])
                # ignore

            elif days[r] > stack[-1]:
                continue

        return len(stack)

           
            # if stack and stack[-1] > item:
            #     res += 1
            #     stack.clear()
            # # else:
            # stack.append(item)


    