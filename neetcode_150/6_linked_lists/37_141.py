
# O(N) linear runtime, O(1) constant space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
    
    
   
# O(N) linear runtime & O(N) linear space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_set = set()
        current = head

        while current:
            if current in hash_set:
                return True

            else:
                hash_set.add(current)
            current = current.next

        return False