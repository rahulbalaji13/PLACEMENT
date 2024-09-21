
/**
 * Definition for singly-linked list.
 1)Assign vector to v and vector contains value in the linked list node
 2)push_back methos used to push elements into a vector from back
 3)rbegin methid is reverse iterator which points the last elemnt of the map and rend method send iterator to end of the element 
 4)Finally ans variable returns the sorted k lists from vector v 
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
       vector<int>v;
       for(int i=0;i<lists.size();i++)
       {
           while(lists[i])
           {
               v.push_back(lists[i]->val);
               lists[i]=lists[i]->next;
           }
       }
       sort(rbegin(v),rend(v));
       ListNode* ans=nullptr;
       for(int i=0;i<v.size();i++)
       {
           ans=new ListNode(v[i],ans);
       }
       return ans;
    }

};
