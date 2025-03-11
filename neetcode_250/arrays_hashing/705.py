

# horribly slow implementation, everything is linear runtime
class MyHashSet:

    def __init__(self):
        self.table = []
        

    def add(self, key: int) -> None:
        hash_key = hash(key)

        key_in_table = False
        for i, (table_key, value) in enumerate(self.table):
            if hash_key == table_key:
                key_in_table = True

        if key_in_table == False:
            self.table.append((hash_key, key))

    
    def remove(self, key: int) -> None:
        hash_key = hash(key)

        for i, (table_key, value) in enumerate(self.table):
            if hash_key == table_key:
                del self.table[i]
        
    def contains(self, key: int) -> bool:
        hash_key = hash(key)

        for i, (table_key, value) in enumerate(self.table):
            if hash_key == table_key:
                return True
        return False


# design hash set
# so this does pass but it's not allowed
class MyHashSet:

    def __init__(self):
        self.table = {}
        

    def add(self, key: int) -> None:
        hash_key = hash(key)

        if hash_key not in self.table:
            self.table[hash_key] = key

    
    def remove(self, key: int) -> None:
        hash_key = hash(key)
        if hash_key in self.table:
            del self.table[hash_key]
        

    def contains(self, key: int) -> bool:
        hash_key = hash(key)
        return hash_key in self.table
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)