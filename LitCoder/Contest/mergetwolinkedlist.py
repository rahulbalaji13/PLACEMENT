class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

def merge_linked_lists(headA, headB):
    dummy = ListNode(0)
    tail = dummy
    
    currentA, currentB = headA, headB
    
    while currentA or currentB:
        if currentA:
            tail.next = ListNode(currentA.value)
            tail = tail.next
            currentA = currentA.next
        
        if currentB:
            tail.next = ListNode(currentB.value)
            tail = tail.next
            currentB = currentB.next
    
    return dummy.next

# Helper function to build linked list from input data
def build_linked_list_from_input(length, input_data):
    linked_list = LinkedList()
    for i in range(length):
        linked_list.append(input_data[i])
    return linked_list

# Reading input from user
print("Enter the length of the first linked list:")
len1 = int(input())
print("Enter the elements of the first linked list:")
list1_values = [input().strip() for _ in range(len1)]

print("Enter the length of the second linked list:")
len2 = int(input())
print("Enter the elements of the second linked list:")
list2_values = [input().strip() for _ in range(len2)]

# Build linked lists
list1 = build_linked_list_from_input(len1, list1_values)
list2 = build_linked_list_from_input(len2, list2_values)

# Merge linked lists
merged_head = merge_linked_lists(list1.head, list2.head)

# Convert merged linked list to list for output
result = []
current = merged_head
while current:
    result.append(current.value)
    current = current.next

# Print the output
print("Merged Linked List:")
for value in result:
    print(value)
