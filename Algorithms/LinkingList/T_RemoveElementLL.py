"""
class ListNode:
    data  = 0
    next = None
    def __int__(self, data = 0, next = None):
        self.data = data
        self.next = next
        """

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        cur = head.next
        prev = head

        while cur is not None:
            if cur.data == prev.data:
                prev.next = cur.next
                cur = cur.next
            else:
                cur = cur.next
                prev = prev.next
                
        return head
