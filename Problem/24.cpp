class ListNode {
public:
    int val;
    ListNode* next;
    ListNode(int v = 0, ListNode* n = nullptr) : val(v), next(n) {}
};
    ListNode* swapPairs(ListNode* head) {
        if(!head || !head->next)
        {
            return head;
        }

        ListNode* prev = head;
        head = head->next;
        ListNode* cur = head;
        while(cur)
        {
            //append prev
            prev->next = cur->next;
            cur->next = prev;
            cur = cur->next;
            //find prev
            prev = prev->next;
            if(!prev || !prev->next)
            {
                break;
            }
            cur->next = prev->next;
            cur = cur->next;

        }

        return head;
    }