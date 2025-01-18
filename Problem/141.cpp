class ListNode
{
public:
    ListNode *next;
    int val;
    ListNode(int value, ListNode *next)
    {
        this->val = value;
        this->next = next;
    }
};

class Solution
{
public:
    bool hasCycle(ListNode *head)
    {
        ListNode *fast = head;
        ListNode *slow = head;
        while (fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast)
            {
                return true;
            }
        }
        return false;
    }
};