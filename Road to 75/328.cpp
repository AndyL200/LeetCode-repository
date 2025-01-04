#include <iostream>

using namespace std;

class ListNode
{
public:
    ListNode *next;
    int val;
    ListNode(ListNode *next = NULL, int val = 0)
    {
        this->next = next;
        this->val = val;
    }
    void append(int value)
    {
        ListNode *current = this;
        while (current->next != NULL)
        {
            current = current->next;
        }
        current->next = new ListNode(NULL, value);
    }
};

ListNode oddEvenList(ListNode *head)
{
    ListNode *odd = head;
    ListNode *even = head->next;
    ListNode *even_head = even;

    while (even != NULL && even->next != NULL)
    {
        odd->next = odd->next->next;
        even->next = even->next->next;
        odd = odd->next;
        even = even->next;
    }
    odd->next = even_head;
    return head;
}
int main()
{

    ListNode *hire = new ListNode(NULL, 17);
    int x[] = {1, 3, 4, 6, 8, 32, 5, 6, 90};
    for (int i : x)
    {
        hire->append(i);
    }
    ListNode temp = oddEvenList(hire);
    ListNode *oddEven = temp.next;
    while (oddEven != NULL)
    {
        cout << oddEven->val << endl;
        oddEven = oddEven->next;
    }
    return 1;
}