/**
Linked List Group Reverse

Difficulty: HardAccuracy: 57.08%Submissions: 240K+Points: 8Average Time: 30m
Given the head a linked list, the task is to reverse every k node in the linked list. If the number of nodes is not a multiple of k then the left-out nodes in the end, should be considered as a group and must be reversed.
Examples:
Input: head = 1 -> 2 -> 2 -> 4 -> 5 -> 6 -> 7 -> 8, k = 4
Output: 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5
Explanation: The first 4 elements 1, 2, 2, 4 are reversed first and then the next 4 elements 5, 6, 7, 8. Hence, the resultant linked list is 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5.
**/

class Solution {
  public:
    Node *reverseKGroup(Node *head, int k) 
    {
        // code here
        int count = k;
        
        Node *prev = NULL;
        Node *curr = head;
        Node *next = NULL;
        
        if(head == NULL)
        
            return NULL;
        
        while(curr != NULL && count > 0)
        {
             next = curr -> next;
             curr -> next = prev;
             prev = curr;
             curr = next;
             count--;
        }
        head -> next = reverseKGroup(next,k);
        return prev;
    }
};
