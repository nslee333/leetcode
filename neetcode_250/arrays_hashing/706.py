# hashmap

# this works since we have more than enough keys, so we don't worry about collisions.

# all constant time, and O(1_000_001) or constant space
class MyHashMap:

    def __init__(self):
        self.map = [-1] * 1_000_001
        
    def put(self, key: int, value: int) -> None:
        self.map[key] = value
        
    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1

# my working but unconcise working linkedlist solution
# so best case is constant time for all fn calls, worse is linear time
# linear space too, since we still have to store all of them
class MyHashMap:

    def __init__(self):
        self.table = [[] for _ in range(10_000)]
        

    def put(self, key: int, value: int) -> None:
        hash = key % len(self.table)
        
        if self.table[hash] != None:

            for table_key, pair in enumerate(self.table[hash]):
                if pair[0] == key:
                    self.table[hash][table_key] = [key,value]
                    return
            self.table[hash].append([key, value])
        else:
            self.table.append([key, value])
        

    def get(self, key: int) -> int:
        hash = key % len(self.table)

        if self.table[hash] != None:
            print(self.table[hash])
            for table_key, pair in enumerate(self.table[hash]):
                if pair[0] == key:
                    return pair[1]
            return -1
        else:
            print("else", self.table[hash])
            return -1
        

    def remove(self, key: int) -> None:
        hash = key % len(self.table)
        if self.table[hash] != None:
            for table_key, pair in enumerate(self.table[hash]):
                if pair[0] == key:
                    self.table[hash].pop(table_key)