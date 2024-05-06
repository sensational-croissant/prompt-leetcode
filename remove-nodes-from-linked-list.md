--------------Arrays & Hashing--------------## Code

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        queue = []

        while(head != None):
            # Remove smaller nodes from queue
            while(queue and head.val > queue[-1].val):
                queue.pop()
            
            # Only append nodes that can no longer be removed
            if(not queue or head.val <= queue[-1].val):
                queue.append(head)

            head = head.next

        # Relink the resultant linked list
        for i, node in enumerate(queue):
            node.next = queue[i+1] if i+1 < len(queue) else None
        return queue[0] if queue else None
```


## Time complexity:
The time complexity is O(n), where n is the total number of nodes in the linked list. This is because each node is visited once in the process, and for each node, any necessary removals or appending of nodes occurs in constant time.

## Space complexity:
The space complexity is also O(n), where n is the total number of nodes in the linked list. This is because we maintain a queue, the size of which can be up to n in the worst case scenario. Each node in the queue requires O(1) space, resulting in a total of O(n) space.

<!-- --------------Two Pointers--------------# Two Pointers

## Code

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

        # Reverse list.
        previous, current = None, head
        while current:
            nxt = current.next
            current.next = previous
            previous, current = current, nxt

        # Remove nodes.
        head = previous
        current = head
        while current and current.next:
            if current.val < current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
```

## Time complexity:

The time complexity is O(n) because we iterate through the linked list twice, once to reverse it and once to remove the nodes. Here, n is the number of the nodes in the linked list.

## Space complexity:

The space complexity is O(1) because we only use a constant amount of space to store our pointers. -->

--------------Sliding Window--------------# Stack

## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        stack = []
        temp_node = head

        while temp_node:
            while stack and stack[-1].val < temp_node.val:
                stack.pop()

            stack.append(temp_node)
            temp_node = temp_node.next

        head = stack[0]
        curr_node = head

        for node in stack[1:]:
            curr_node.next = node
            curr_node = node

        curr_node.next = None

        return head
```

## Time complexity:
The time complexity of the solution is O(n), where n is the number of nodes in the linked list. The use of stack ensures that each node is visited exactly once. 

## Space complexity:
In the worst case scenario, the space complexity is O(n), as all nodes might have to be stored in the stack.

--------------Binary Search--------------# Reverse Singly-Linked list and keep track of maximum node

## Code

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_max = float('-inf')
        dummy = ListNode(0)

        # reversing the list
        stack = []
        while head:
            stack.append(head)
            head = head.next
            
        while stack:
            node = stack.pop()
            if node.val >= current_max:
                node.next = dummy.next
                dummy.next = node
                current_max = node.val
            else:
                node.next = None
                
        return dummy.next
    
```

## Time complexity: 
O(n), where n is the number of nodes in the linked list, because we must process each node exactly once.

## Space complexity: 
O(n), where n is the number of nodes in the linked list, because in the worst case, all of them could be kept in the stack before they are re-attached to the final list.


<!-- --------------Backtracking--------------# Backtracking

## Code

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(0)
        newHead.next = head
        currNode = newHead
        maxNode = head
        maxVal = head.val
        while currNode.next != None:
            if currNode.next.val < maxVal:
                currNode.next = currNode.next.next
            else:
                if currNode.next.val > maxNode.val:
                    maxNode = currNode.next
                    maxVal = currNode.next.val
                currNode = currNode.next
        maxNode.next = None
        return newHead.next
```

## Time complexity:
The time complexity of the solution is O(n) because we are traversing all the elements of the linked list only once, where n is the number of nodes in the linked list.

## Space complexity:
The space complexity of the solution is O(1) because we are using only a constant amount of extra space, regardless of the input size. -->

<!-- --------------Graphs--------------## Code

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # reverse the linked list
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # remove nodes which have a greater value node on right side
        current = prev
        max_val = prev.val
        while current and current.next:
            if current.next.val < max_val:
                current.next = current.next.next
            else:
                current = current.next
                max_val = current.val

        # return head of modified list
        return prev
```

## Time complexity:

The time complexity is O(n) because we loop through the linked list twice. In the first pass, we reverse the linked list. In the second pass, we remove nodes which have a greater value node on the right side.

## Space complexity:

The space complexity is O(1). We are just using a few pointers, and we are not using any extra data structure such as an array or a hash map. -->

<!-- --------------Advanced Graphs--------------## Code

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
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        head= prev
        # remove nodes
        curr = head
        while curr.next:
            if curr.val >= curr.next.val:
                curr = curr.next
            else:
                curr.next = curr.next.next
        return head
```

## Time complexity:
The time complexity is O(n) because there is only one iteration through the linked list, where n is the number of nodes in the list.

## Space complexity:
The space complexity is O(1) because no additional space is required. -->

<!-- --------------1-D Dynamic Programming--------------# 1-D Dynamic Programming

## Code

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
        max_on_right = head.val
        node = head
        pre_nodes = []

        # Iterate through all nodes from right to left and remove nodes that are smaller
        while node and node.next:
            if node.next.val >= max_on_right:
                max_on_right = node.next.val
                node = node.next
            else:
                pre_nodes.append(node)
                node.next = node.next.next

        # Remove nodes that are to the left of maximum node and smaller
        while pre_nodes and pre_nodes[-1].next.val < max_on_right:
            pre_nodes.pop().next = None

        return head
```

## Time complexity:

The time complexity of this solution is O(N), where N is the length of the linked list since we need to iterate over the list.

## Space complexity:

The space complexity of this solution is also O(N), due to the additional space required by stack 'pre_nodes'. -->

<!-- --------------2-D Dynamic Programming--------------# Linear Time Complexity

## Code

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0)
        dummy = prev
        dummy.next = head
        maxval = head.val

        while head and head.next:
            if maxval < head.next.val:
                maxval = head.next.val
            if head.val < maxval:
                prev.next = head.next
                head = head.next
            else:
                prev = prev.next
                head = head.next

        if head and head.val < maxval:
            prev.next = None
        return dummy.next
``` 

## Time complexity:
The time complexity is O(n) because we only perform a single pass over the linked list. Here, n refers to the number of nodes in the linked list.

## Space complexity:
The space complexity is O(1), as we are not using any additional space that scales with the input size. -->

--------------Greedy--------------# Greedy

## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr = self.removeNodes(head.next)
        if curr.val > head.val:
            return curr

        head.next = curr
        return head
```

## Time complexity:

The time complexity is O(n^2), where n is the number of nodes in the linked list since we need to parse each node and compare it with all other nodes to the right of it.

## Space complexity:

The stack space due to the recursive calls adds up to O(n) space complexity. This is because we may end up calling the recursive function n times, which would take up O(n) space on the stack.

--------------Intervals--------------## Intervals

For example, if the head given is `[5,2,13,3,8]`, we would remove the nodes that are smaller than the maximum node to its right. That is `5`, `2`, and `3` should be removed as `13` is greater than them and is located to their right. `8` is the maximum to its right. Thus, we return the head `[13,8]`.

By iterating from the end of the list to the start, we can keep track of the maximum found so far, and add a node to the new linked list we create only if its value is equal to the maximum.

## Code

``` python
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        maxNode = 0
        newTail = None
        current = head
        nodes = []
        while current:
            nodes.append(current)
            current = current.next

        for node in reversed(nodes):
            if maxNode <= node.val:
                maxNode = node.val
                node.next = newTail
                newTail = node

        return newTail
```

## Time complexity:

The time complexity is O(n), where n refers to the number of nodes in the linked list. This is because we're performing a single pass over the all nodes in the linked list.

## Space complexity:

The space complexity is O(n), where n refers to the number of nodes in the linked list. This is because we're storing all nodes of the linked list in an array for reversed iterating.

--------------Math & Geometry--------------# Math & Geometry

## Code

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

        new_head = self.removeNodes(head.next)
        if head.val < new_head.val:
            return new_head
        else:
            head.next = new_head
            return head
```

## Time complexity:
The time complexity of this function is O(n), where n is the number of nodes in the list. This is because each call to removeNodes visits exactly one node, and there are n nodes to visit in total.

## Space complexity:
The space complexity of this function is O(n), where n is the number of nodes in the list. This is because each recursive call to removeNodes adds a new layer to the system call stack, and there are n recursive calls in the worst case scenario.



<!-- --------------Bit Manipulation--------------# Linked List

## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        maxval = -1
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        max_node = dummy
        while cur and cur.next:
            if cur.next.val >= maxval:
                maxval = cur.next.val
                max_node = cur
            cur = cur.next        
        max_node.next = None
        return dummy.next
```

## Time complexity:

The time complexity is O(n) because we traverse the linked list once where n is the number of nodes in the linked list.

## Space complexity:

The space complexity is constant O(1) because we are using finite amount of space for a few variables. Our algorithm does not use any extra space proportional to the size of the linked list.
 -->
