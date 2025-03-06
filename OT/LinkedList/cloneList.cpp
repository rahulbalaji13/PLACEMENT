/**
CLONE LIST WITH NEXT AND RANDOM POINTER 

Difficulty: HardAccuracy: 64.8%Submissions: 108K+Points: 8
You are given a special linked list with n nodes where each node has two pointers a next pointer that points to the next node of the singly linked list, and a random pointer that points to the random node of the linked list.

Construct a copy of this linked list. The copy should consist of the same number of new nodes, where each new node has the value corresponding to its original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list, such that it also represent the same list state. None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

NOTE : Original linked list should remain unchanged.
**/

class Solution 
{
  public:
    Node *cloneLinkedList(Node *head) 
    {
        // Attach the clone node in between the curr and temp nodes
        Node* curr = head;
        while(curr)
        {
            Node *cloneNode = new Node(curr -> data);
            Node *temp = curr -> next;
            curr -> next = cloneNode;
            cloneNode -> next = temp;
            curr = curr -> next -> next;
        }
        
        //Attach the random pointers
        curr = head;
        
        while(curr)
        {
            if(curr -> random)
            
               curr -> next -> random = curr -> random -> next;
               curr = curr -> next -> next;
        }
        
        // Attach the next pointers
        Node *clone = new Node(-1); //Clone is the kind of pointer that can be used to point the next node by the clone node
        curr = head;
        Node *temp = clone; //clone similar to next pointer for clone node 
        while(curr)
        {
            temp -> next = curr -> next;
            curr -> next = curr -> next -> next;
            temp = temp -> next;
            curr = curr -> next;
        }
         return clone -> next;
    }
};
