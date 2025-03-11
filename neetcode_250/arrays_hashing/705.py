# hash set


# with neetcode hint, constant time best case O(1), linear runtime O(N) worst case if bucket (linked list) has N elements
# linear space O(n)
class MyHashSet:

    def __init__(self):
        self.arr = [None] * 10_000 


    def add(self, key: int) -> None:
        hash = int(key % len(self.arr))

        if self.arr[hash]:
            current = self.arr[hash]
            prev = None
            while current:
                if current.val == key:
                    return
                prev = current
                current = current.next
            node = ListNode()
            node.val = key
            prev.next = node
        else:
            self.arr[hash] = ListNode()
            self.arr[hash].val = key
  
    def remove(self, key: int) -> None:
        hash = int(key % len(self.arr))

        if self.arr[hash]:
            current = self.arr[hash]
            prev = None
            while current:
                if current.val == key:
                    if prev:
                        prev.next = prev.next.next
                    else:
                        self.arr[hash] = current.next
                prev = current
                current = current.next
 
 
    def contains(self, key: int) -> bool:
        hash = int(key % len(self.arr))


        if self.arr[hash]:
            current = self.arr[hash]
            while current:
                if current.val == key:
                    return True
                current = current.next
        return False

# better idea with binary search
class MyHashSet:

    def __init__(self):
        self.arr = []

    # log n
    def binary_search(self, arr: list, target: int) -> int:

        l, r = 0, len(arr) - 1
        mid = l + r // 2

        while l <= r:
            mid = (l + r) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                mid
            
        return -1

    # log n & n log n
    def add(self, key: int) -> None:

        i = self.binary_search(self.arr, key)

        if i == -1:
            self.arr.append(key)

        self.arr = sorted(self.arr)

    # log n
    def remove(self, key: int) -> None:

        i = self.binary_search(self.arr, key)

        if i == -1: 
            return None
        else:
            del self.arr[i]

    # log n
    def contains(self, key: int) -> bool:

        i = self.binary_search(self.arr, key)

        if i == -1:
            return False
        return True









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