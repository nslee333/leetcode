def test(s, t):
    
    hash = {}
    for i in range(len(t)):
        if hash.get(t[i]): 
            hash[t[i]] += 1
        else: 
            hash[t[i]] = 1
    # # all_zero_values = all(value == 0 for value in hash.values())
    res, temp  = [], []
    l = 0
    r = 0
    while r < len(s):
        # print(temp)
        print(res)
        print(l, "l")
        print(r, "r")
        # print(hash.values())
        if all(value == 0 for value in hash.values()):
            res.append([len(temp), "".join(temp)])
            temp.clear()
            if hash.get(s[l]) == 0:
                hash[s[l]] += 1
            l += 1
            r = l
        elif hash.get(s[r]):
            hash[s[r]] -= 1
        temp.append(s[r])
        # this isn't right, b/c we only want to add non-t chars after we've seen one.
        r += 1
    
    
    if len(res) > 0:
        x = min(res)
        return x
    else:
        return ""
            
       



if __name__ == '__main__':
    print(test("ADOBECODEBANC", "ABC"))