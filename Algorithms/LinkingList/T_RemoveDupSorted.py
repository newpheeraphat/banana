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
                
