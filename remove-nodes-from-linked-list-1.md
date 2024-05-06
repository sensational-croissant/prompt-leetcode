--------------Stack--------------# Stack

## Code

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        stack = []
        cur = head
        while cur:
            while stack and stack[-1].val < cur.val:
                stack.pop()
            stack.append(cur)
            cur = cur.next

        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]

        stack[-1].next = None
        return stack[0]
```


## Time complexity: O(n)
The time complexity is O(n) because we iterate through the linked list once.

## Space complexity: O(n)
The space complexity is O(n) because we store nodes in the stack. In the worst case, the size of the stack could be the same as the number of nodes in the linked list.

--------------Heap / Priority Queue--------------# Heap / Priority Queue

## Code

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        stack = []
        current = head
        while current:
            while stack and stack[-1].val < current.val:
                stack.pop()
            stack.append(current)
            current = current.next
        
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
        
        stack[-1].next = None
        return stack[0]
```


## Time complexity:
The time complexity is O(n) where n is the number of nodes in the linked list.

## Space complexity:
The space complexity is O(n) where n is the number of nodes in the linked list, due to the stack used to track nodes.



<!-- --------------Linked List--------------# Linked List

## Code

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        
        while curr:
            nxt = curr.next
            remove = False
            while nxt:
                if nxt.val > curr.val:
                    remove = True
                    break
                nxt = nxt.next
            if remove:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = nxt
        
        return dummy.next
```

## Time complexity: O(n^2)
The time complexity is O(n^2) where n is the number of nodes in the linked list because for each node, we potentially iterate through the remaining nodes to check for a greater value.

## Space complexity: O(1)
The space complexity is O(1) because we are using a constant amount of extra space, regardless of the input size.

--------------Trees--------------# Trees

## Code

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        elif not head.next:
            return head
        
        dummy = ListNode(float('-inf'))
        dummy.next = head
        prev = dummy
        curr = head
        
        while curr and curr.next:
            if curr.next.val < curr.val:
                temp = curr.next
                curr.next = temp.next
                temp.next = None
            else:
                curr = curr.next
                prev = prev.next
        
        return dummy.next
```

## Time complexity:
The time complexity is O(n) where n is the number of nodes in the linked list.

## Space complexity:
The space complexity is O(1) as we are using constant extra space regardless of the input size.

--------------Tries--------------# Tries

1. Traverse the linked list and for each node, check if there is any node with a greater value to its right. If yes, remove the current node.
2. Use a stack to keep track of the nodes with decreasing values.

## Code

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        stack = []
        current = head
        prev = None
        
        while current:
            while stack and stack[-1].val < current.val:
                stack.pop()
            if not stack:
                prev = current
            else:
                prev.next = current.next
            stack.append(current)
            current = current.next
        
        return head
```

## Time complexity:
The time complexity is O(n) where n is the number of nodes in the linked list.

## Space complexity:
The space complexity is O(n) in the worst case where all the nodes are in decreasing order of values. -->

