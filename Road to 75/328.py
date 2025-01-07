
class ListNode:
   
    def __init__(self, val=0, next=None):
          self.val = val
          self.next = next



def oddEvenList(head: ListNode) -> ListNode:
        
        
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        odd.next = even_head

        return head


LastList = ListNode(9)
NextList = ListNode(4, LastList)
ThisList = ListNode(8, NextList)
node_list = ListNode(5, ThisList)

finalList = oddEvenList(node_list)
while finalList:
    print(finalList.val)
    finalList = finalList.next