--------------Stack--------------# Stack

## Code

```python
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
The time complexity of this solution is O(n), where n is the number of nodes in the linked list.

## Space complexity:
The space complexity of this solution is O(n), where n is the number of nodes in the linked list.--------------Linked List--------------# Linked List

## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current:
            remove = False
            runner = current.next
            while runner:
                if runner.val > current.val:
                    remove = True
                    break
                runner = runner.next
            
            if remove:
                prev.next = current.next
            else:
                prev = current
            
            current = current.next
        
        return dummy.next
```

## Time complexity:
The time complexity of this solution is O(n^2), where n is the number of nodes in the linked list.

## Space complexity:
The space complexity is O(1) as we are using constant extra space.--------------Trees--------------# Trees

## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current.next:
            if current.next.val > current.val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        
        if current.val < prev.val:
            prev.next = None
        
        return dummy.next
```

## Time complexity:
The time complexity of this solution is O(n), where n is the number of nodes in the linked list.

## Space complexity:
The space complexity is O(1) as we are using constant extra space.--------------Tries--------------### Tries

1. Traverse the linked list and for each node, check if there exists a node with a greater value to its right.
2. If such a node exists, remove the current node from the linked list.
3. Return the head of the modified linked list.

### Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current:
            remove = False
            temp = current.next
            while temp:
                if temp.val > current.val:
                    remove = True
                    break
                temp = temp.next
            
            if remove:
                prev.next = current.next
            else:
                prev = current
            
            current = current.next
        
        return dummy.next
```

### Time complexity:
The time complexity of this solution is O(n^2), where n is the number of nodes in the linked list.

### Space complexity:
The space complexity of this solution is O(1) as we are using constant extra space.--------------Heap / Priority Queue--------------# Heap / Priority Queue

## Code

```python
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
The time complexity of this solution is O(n), where n is the number of nodes in the linked list.

## Space complexity:
The space complexity of this solution is O(n) due to the stack used to keep track of nodes with decreasing values.