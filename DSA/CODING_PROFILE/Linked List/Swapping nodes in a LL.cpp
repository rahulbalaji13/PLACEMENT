
/**Steps to solve: 1)Find the length of LL 
                   2)Make two pointer 
                   3)run slow k times and fast n-k, so that they are on target locations 
                   4)Just swap
**/

 
 struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
 
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
          ListNode* fast=head,*slow=head,*curr=head;
          int n=0;
          while(curr){curr=curr->next;n++;}
          n=n-k;
          while(n--)fast=fast->next;
          k--;
          while(k--)slow=slow->next;
          swap(slow->val,fast->val);
          return head;
    }
};
};