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
    public ListNode oddEvenList(ListNode head) 
    {
       if(head == null || head.next == null)
           return head;
       
       //Note that the relative order inside both the even and odd groups should remain as it was in te output.   
       ListNode odd = head;
       ListNode even  = head.next;
       ListNode temp = even;
       
       while(even != null && even.next != null)
       {
         //You must solve extra O(1) space complexity and swap operation suits that complexity
         odd.next = even.next;
         odd = odd.next;
         even.next = odd.next;
         even = even.next;
       }
         odd.next = temp;
         return head;
    }
}
