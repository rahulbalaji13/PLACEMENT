/*** Merge two list
1)Create two lists
2)Change as list 1 point to null then return list 2 vice versa...
3)Point the list 1 and list 2 to the value
4)Use mergeTwoLists method in cpp to perform merge operation
5)Return the list1 and list2
*/
  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };
 
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1==NULL)
        {  
         return list2;
        }
        if(list2==NULL)
        { 
          return list1;
        }
        if(list1->val <= list2->val)
        {
            list1->next=mergeTwoLists(list1->next,list2);
            return list1;
        }
        else
        {
            list2->next=mergeTwoLists(list1,list2->next);
            return list2;
        }
    }
};
