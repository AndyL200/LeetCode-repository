#include <iostream>
using namespace std;

class ListNode {
    public:
    ListNode* next;
    int val;
    ListNode(ListNode* nxt = nullptr, int value = 0) 
    {
        next = nxt;
        val = value;
    }
};

ListNode* rotateRight(ListNode* head, int k) {
    if(!head || k <= 0)
    {
        return head;
    }
    int len = 1;
    k-=1;
    
    ListNode* current = head;
    ListNode* prev = nullptr;
    ListNode* bracer = current;
    while (k)
    {
        if(!bracer->next){
            break;
        }
        bracer = bracer->next;
        len+=1;
        k-=1;
    }
    while (bracer->next != nullptr)
    {
        prev = current;
        current = current->next;
        bracer = bracer->next;
        len+=1;
    }
    if(prev)
    {
        prev->next = nullptr;
        bracer->next = head;
    }
    else
    {
        bracer->next = nullptr;
    }
    head = current;
    if (k)
    {
        return rotateRight(head, (k - 1) % len);
    }

    return head;
};


int main()
{
    ListNode* res = rotateRight(new ListNode(new ListNode(new ListNode(new ListNode(new ListNode(nullptr, 5), 4), 3), 2), 1), 2);
    while(res)
    {
        printf("%d::", res->val);
        res = res->next;
    }
    return 0;
}