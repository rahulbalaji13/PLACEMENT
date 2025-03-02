/**
234. Palindrome Linked List
(Easy Level)
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
Follow up: Could you do it in O(n) time and O(1) space?
**/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution 
{
    public boolean isPalindrome(ListNode head) 
    {
      //Find the middle element 
      ListNode slow = head;
      ListNode fast = head;
      while(fast.next != null && fast.next.next != null)
      {
        slow = slow.next;
        fast = fast.next.next;
      }

      //Reverse the list
      ListNode prev = null;
      ListNode curr = slow;
      if(curr != 0)
      {
        ListNode next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
      }

      //Print the true or false for palindrome and non palindrome list 
      while(prev.val != null)
      {
        if(prev.val != head.val)
          return false;
          curr = curr.next;
          head = head.next;
      }
      return true;
      }
}

      
