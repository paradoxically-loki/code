# DSA Notes in Python

## Arrays
### Static Arrays
- Fixed size, decided at the time of creation, allocated as a contiguous block of memory. 
- Access by index is $O(1)$.
- Insertion/deletion in the middle is $O(n)$, as a lot of values need to be shifted.
- numpy.ndarrays are static arrays, resizing means allocating a new array, not just growing the previous one.
- Python lists/arrays are dynamic in size.
### Dynamic Arrays
- Same contiguous memory idea, but it can resize. 
- If we exceed the size, it creates a new list double the size and copies everything over.
- Append time is $O(1)$ *amortized* and not $O(1)$ *flat* like we have in static arrays.
- Appending at the friend is anyway $O(n)$ in both cases, as we have to shift the entire list.

### Some important features/functions for Arrays
**Access**
- `arr[i]` -> access. $O(1)$
- `len(arr)` -> $O(1)$, Python lists track their length. Not counted each time.
- `arr[a:b]` -> Slicing, $O(k)$. Creates a new list, doesn't just view the original.

**Adding Elements**
- `arr.append(x)` -> $O(1)$ amortized. Adds at the end.
- `arr.extend(iterable)` -> $O(k)$ amortized. Adds each element of another iterable.
- `arr.insert(i,x)` -> $O(n)$, everything from the index onwards need to be shifted.

**Removing Elements**
- `arr.pop()` -> $O(1)$, removes from the end, not shift needed.
- `arr.pop(i)` -> $O(n)$, everything past the index needs to be changed.
- `arr.remove(x)` -> $O(n)$, searches for the first match, then shifts.
- `del arr[i]` -> $O(n)$, same cost as pop.
- `arr.clear()` -> $O(n)$.

**Search**
- `x in arr` -> $O(n)$, linear search.
- `arr.index(x)` -> $O(n)$, returns position.
- `arr.count(x)` -> $O(n)$

**Reordering**
- `arr.sort()` -> $O(n \log(n))$, TimSort under the hood, stable.
- `sorted(arr)` -> $O(n \log(n))$, returns a new list, instead on in-place sorting.
- `arr.reverse()` -> $O(n)$.
- `arr[::-1]` -> $O(n)$, same idea, but returns a new list.

**Combining**
- `arr1 + arr2` -> $O(n+m)$, creates a new list.
- `arr*k` -> $O(nk)$.

**Note**
- `pop(0)`, and `insert(0,x)` are $O(n)$ and not $O(1)$, as we have to shift the whole list.

### Implementation of a Dynamic Array
```python
class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0]*self.capacity

    def get(self, i: int) -> int:
        if not 0 <= i <= self.capacity-1:
            raise IndexError('Index out of range')
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        self.capacity = 2*self.capacity
        new_arr = [0]* self.capacity

        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.length
        
    def getCapacity(self) -> int:
        return self.capacity

```

## Linked Lists
### Basic Structure
```python
# linked lists
from typing import List

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head
        i = 0
        while i < index and temp:
            temp = temp.next
            i += 1
        return temp.data if temp else -1

    def insertHead(self, val: int) -> None:
        temp = self.head
        self.head = Node(val)
        self.head.next = temp

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(val)

    def remove(self, index: int) -> bool:
        if not self.head or index < 0:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        curr = self.head
        i = 0
        while curr.next and i < index - 1:
            curr = curr.next
            i += 1
        if curr.next is None:
            return False
        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result
```

### Reversing a Linked List
```python
def reverseLL(head: Node) -> Node:
    prev, current = None, head

    while current:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    
    return prev
```

### Detecting Cycle
```python
def detectCycle(head: Node) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next

        if (slow == fast): return True
    
    return False
```

## Stack
### Stack Basics
```python

```




## Queue
### Queue Basics
```python

```


## Binary Trees
### Binary Trees Basics
```python
# class for TreeNode
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# adding stuff
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
```
### Binary Trees Traversal
```python
# Preorder Travesal - DFS
def preorder_dfs(root: TreeNode) -> None:
    if root:
        print(root.data, end=" ")
        preorder_dfs(root.left)
        preorder_dfs(root.right)
```

```python
# Inorder Traversal - DFS
def inorder_dfs(root: TreeNode) -> None:
    if root:
        inorder_dfs(root.left)
        print(root.data, end=" ")
        inorder_dfs(root.right)
```

```python
# Postorder Traversal - DFS
def postorder_dfs(root: TreeNode) -> Node:
    if root:
        postorder_dfs(root.left)
        postorder_dfs(root.right)
        print(root.data, end=" ")
```

```python
# BFS Travesal using Queue
from collections import deque
def bfs(root: TreeNode) -> None:
    if not root: return 

    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
```
### Constructing a Binary Tree
```python
```

### Height of a Binary Tree
```python
def height(root: TreeNode) -> int:
    if not root: return 0

    leftHt = height(root.left)
    rightHt = height(root.right)

    return 1 + max(leftHt, rightHt)
```

### Number of Nodes in a Binary Tree
```python
def numNodes(root: TreeNode) -> int:
    if not root: return 0

    leftNums = numNodes(root.left)
    rightNums = numNodes(root.right)

    return 1 + leftNums + rightNums
```

### Is Identical
```python
def isIdentical(p: TreeNode, q: TreeNode) -> bool:
    if not p or not q: return p == q

    return (
        p.data ==  q.data and
        isIdentical(p.left, q.left) and
        isIdentical(p.right, q.right)   
    )
```
### Is Subtree
```python
def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:

    if not subroot: return True
    if not root: return False
    
    if (root.data == subRoot.data and isIdentical(root, subRoot)): return True

    return (
        isSubtree(root.left, subRoot) or
        isSubtree(root.right, subRoot)
    )
```

