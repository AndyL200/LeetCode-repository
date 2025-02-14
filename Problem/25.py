def reverseKGroup(self, head, k):
    """
    :type head: Optional[ListNode]
    :type k: int
    :rtype: Optional[ListNode]
    """
    curr = head
    start = head
    end = None
    prev = None
    c = 1
    while curr:
        if c == k:
            end = curr
            prev = start
            while start != end:
                t = start.next
                start.next = end.next
                end.next = start
                start = t
            head = end
            start = prev.next
            curr = prev.next
        elif c % k == 0:
            end = curr
            prev.next = end
            prev = start
            while start != end:
                t = start.next
                start.next = end.next
                end.next = start
                start = t
            start = prev.next
            curr = prev.next
        else:
            curr = curr.next
        c+=1
    return head