--------------Stack--------------# Stack

<!-- ## Code

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head:
            while nodes and head.val > nodes[-1].val:
                nodes.pop()
            nodes.append(head)
            head = head.next
        if not nodes:
            return None
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        nodes[-1].next = None
        return nodes[0]
        
```

## Time complexity:

The time complexity is O(n) where n is the number of nodes in the LinkedList. We are walking through the LinkedList once.

## Space complexity:

The space complexity is also O(n) as in the worst case scenario, every node of the list will be inserted into the stack.

--------------Linked List--------------# Linked List -->

## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            while stack and stack[-1].val < head.val:
                stack.pop()
            stack.append(head)
            head = head.next
        if not stack:
            return None
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
        stack[-1].next = None
        return stack[0]
```

## Time complexity:
The time complexity of the approach is `O(n)` because in the worst case scenario we go through every element in the linked list, where `n` is the length of the linked list. The `while` loop inside the main loop brings some complexity but it just decreases the size of the stack, it does not result in a `O(n^2)` time complexity.

## Space complexity:
The space complexity of the approach is `O(n)`, as we are using a stack to store the elements of the linked list. The stack may store all elements of the linked list in the worst case, so the size of the stack is proportional to the size of the linked list.

--------------Trees--------------## Code

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # reverse the list
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # remove nodes
        newHead = prev
        while prev.next:
            if prev.val > prev.next.val:
                prev.next = prev.next.next
            else:
                prev = prev.next

        return newHead
```

## Time complexity: 

The time complexity for reversing the linked list is O(n) and removing nodes is also O(n). Thus, the total time complexity is O(n).

## Space complexity: 

The space complexity is O(1) as no additional space is used.

--------------Tries--------------# Tries

## Code

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the list
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        # traverse the reversed list
        dummy = ListNode(0)
        dummy.next = prev
        max_val = prev.val
        current = prev.next
        prev = dummy
        while current:
            # if the node's value is less than max_val, delete it
            if current.val < max_val:
                prev.next = current.next
            else:
                # if the node's value is greater than or equal to max_val, update max_val and move the prev pointer
                max_val = current.val
                prev = current
            current = current.next

        return dummy.next
```

## Time complexity:

The time complexity is O(n) because we only traverse the list twice.

## Space complexity:

The space complexity is O(1) because we only use a fixed amount of space to store the dummy node and pointers.

--------------Heap / Priority Queue--------------# Stack

## Code

``` python
class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        result = ListNode(0)
        result.next = head
        stack = [result]
        
        while head and head.next:
            if head.val < head.next.val:
                node = stack.pop()
                node.next = head.next
            else:
                stack.append(head)
            head = head.next
        
        node = stack.pop()
        node.next = None
        
        return result.next
```

## Time complexity:
- To traverse the linked list, the time complexity is linear, i.e., O(n) where n is the number of nodes.

## Space complexity:
- We use auxiliary space to store the stack and the result which can go up to n elements. Hence, space complexity is O(n).

