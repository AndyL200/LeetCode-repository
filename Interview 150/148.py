class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    if not head:
        return None
    n = 0
    cur = head
    m = head
    while cur.next:
        if m.val < cur.val:
            m = cur
        cur = cur.next
        n+=1

    if n <= 1:
        return head

        
    if cur.val < m.val:
        t = ListNode(m.val, cur.next)
        cur.next = t
        m.val = m.next.val
        m.next = m.next.next
    

    while n > 1:
        i = 1
        cur = head
        m = head
        
        while i < n:
            if not m or m.val < cur.val:
                m = cur
            cur = cur.next
            i+=1 
        
        if cur.val < m.val:
            t = ListNode(m.val, cur.next)
            cur.next = t
            m.val = m.next.val 
            m.next = m.next.next   
            
        n -= 1

    return head


t = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
res = sortList(t)
while res:
    print(res.val)
    res = res.next