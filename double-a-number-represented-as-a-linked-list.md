```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseLinkedList(head):
            prev = None
            curr = head
            while curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev
        
        reversed_head = reverseLinkedList(head)

        carry = 0
        current = reversed_head
        while current:
            current.val = current.val * 2 + carry
            carry = current.val // 10
            current.val %= 10
            current = current.next

        if carry:
            new_node = ListNode(carry)
            new_node.next = reversed_head
            reversed_head = new_node

        return reverseLinkedList(reversed_head)
``` 

You can now create an instance of the `Solution` class and call the `doubleIt` method by passing the head of the linked list to double it as per the described algorithm.```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseLinkedList(head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        reversed_head = reverseLinkedList(head)
        
        carry = 0
        current = reversed_head
        while current:
            doubled_val = current.val * 2 + carry
            current.val = doubled_val % 10
            carry = doubled_val // 10
            if current.next is None and carry > 0:
                current.next = ListNode(carry)
                break
            current = current.next
        
        return reverseLinkedList(reversed_head)
```

You can use this `doubleIt` method in the Solution class to double a number represented as a linked list.