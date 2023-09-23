class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) == len(t):
            return False

        # this is used for the follow up question, haven't tested it :-)

        # if len(s) > len(t):
        #     if len(t) == 0:
        #        return True
        #     sub_arr, og_arr = list(t), list(s)
        # else:
        #     sub_arr, og_arr = list(s), list(t)

        sub_arr, og_arr = list(s), list(t)
        og_pointer, sub_pointer = 0, 0

        while og_pointer < len(og_arr):
            print(sub_pointer)
            if sub_pointer == len(sub_arr):
                break
            elif og_arr[og_pointer] == sub_arr[sub_pointer]:
                og_pointer += 1
                sub_pointer += 1
            else:
                og_pointer += 1
        return sub_pointer == len(sub_arr)