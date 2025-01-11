def pairSum(head: ListNode) -> int:     

    d = deque()

    current = head
    n = 0
    while current:
        d.append(current.val)
        current = current.next
        n += 1

    maximum = head.val
    while d:
        temp = d.popleft() + d.pop()
        if maximum < temp:
            maximum = temp
            
    return maximum