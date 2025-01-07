def reverseList(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    current = head
    if not current:
        return head
    while current.next:
        current = current.next
    new_head = current
    while head != new_head:
        temp = head
        head = temp.next
        temp.next = new_head.next
        new_head.next = temp
    
    return new_head