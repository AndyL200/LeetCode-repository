#include <iostream>
struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

    void removeLeadingZeroes(ListNode* l)
    {   if(!l) {
        return;
        }
        while(l && l->val == 0)
        {
            l = l->next;
        }
        return;
    }
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* first = l1;
        ListNode* second = l2;
        removeLeadingZeroes(l1);
        removeLeadingZeroes(l2);
        ListNode* fin = new ListNode();
        ListNode* finPoint = fin;
        int carry = 0;
        while(first && second)
        {
            int combine = first->val + second->val;
            if (finPoint->val+combine >= 10)
            {
                carry = (finPoint->val+combine)/10;
                finPoint->val = (finPoint->val+combine) % 10;
                finPoint->next = new ListNode(carry);
            }
            else {
                carry = 0;
                finPoint->val += combine;
                if(first->next || second->next) {
                    finPoint->next = new ListNode();
                }
            }
            finPoint = finPoint->next;
            first = first->next;
            second = second->next;

        }
        while(first){
            int combine = first->val;
            if (finPoint->val+combine >= 10)
            {
                carry = (finPoint->val+combine)/10;
                finPoint->val = (finPoint->val+combine) % 10;
                finPoint->next = new ListNode(carry);
            }
            else {
                carry = 0;
                finPoint->val += combine;
                if(first->next) {
                    finPoint->next = new ListNode();
                }
            }
            finPoint = finPoint->next;
            first = first->next;
        }
        while(second){
            int combine = second->val;
            if (finPoint->val+combine >= 10)
            {
                carry = (finPoint->val+combine)/10;
                finPoint->val = (finPoint->val+combine) % 10;
                finPoint->next = new ListNode(carry);
            }
            else {
                carry = 0;
                finPoint->val += combine;
                if(second->next) {
                    finPoint->next = new ListNode();
                }
            }
            finPoint = finPoint->next;
            second = second->next;
        }
        return fin;
    }
int main() {
    ListNode* uno = new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9)))))));
    ListNode* dos = new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9))));
    ListNode* res = addTwoNumbers(uno, dos);
    while(res){
        std::cout << res->val << '\n';
        res = res->next;
    }
}