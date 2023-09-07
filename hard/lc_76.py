def hash_fn(t):
    hash = {}
    for i in range(len(t)):
        if hash.get(t[i]): 
            hash[t[i]] += 1
        else: 
            hash[t[i]] = 1
    return hash



def test(s, t):
    
    hash = hash_fn(t)
    
    res, temp  = [], []
    l = 0
    r = 0
    t_seen = False
    while l < len(s):
        # print(len(s))
        print(l, "l", r, "r")
        if r >= len(s): break
        if all(value == 0 for value in hash.values()):
            res.append([len(temp), "".join(temp)])
            temp.clear()
            
            if hash.get(s[l]) == 0:
                hash[s[l]] += 1
            hash = hash_fn(t)
                
            l += 1
            r = l
            t_seen = False
            
        elif hash.get(s[r]):
            hash[s[r]] -= 1
            t_seen = True
            
        if t_seen:
            temp.append(s[r])
        
        # ^ Now we're not fully exploring the array since r never
        r += 1
    
    
    if len(res) > 0:
        x = min(res)
        return x
    else:
        return ""
            
       

if __name__ == '__main__':
    print(test("ADOBECODEBANC", "ABC"))