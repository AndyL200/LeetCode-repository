class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

def partition(head, x):
    before, after = ListNode(0), ListNode(0)
    before_cur, after_cur = before, after

    while head:
        if head.val < x:
            before_cur.next = head
            before_cur = before_cur.next
        else:
            after_cur.next = head
            after_cur = after_cur.next
        head = head.next
    after_cur.next = None
    before_cur.next = after.next
    return before.next