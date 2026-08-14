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

## Queue
### Introduction
- FIFO (First In, First Out) functionality
- Heavily used in Graph BFS Traversals. `List.pop(0)` if $O(n)$, so, simple lists won't be feasible.
- We mostly use the `deque` (pronounced as deck) functionality from `collections` library.
### Some important features/functions on `deque`
```python
from collections import deque
d = deque([1,2,3])
```
- `d.append(4)` -> $O(1)$, appends to the right.
- `d.appendleft(0)` -> $O(1)$, appends to the left.
- `d.pop()` -> $O(n)$, removes and return the rightmost element.
- `d.popleft()` -> $O(1)$, removes and return the leftmost element.
- `d.extend(iterable)` -> $O(k)$, appends multiple elements to the right.
- `d.extendleft(iterable)` -> $O(k)$, appends multiple elements to the right (in the reverse order).
- `d.insert(i,x)` -> $O(n)$, inserts $x$ at index $i$.
- `d.remove(x)` -> $O(n)$, removes the first occurence of $x$.
- `d.rotate(n)` -> $O(k)$, rotates by $n$ steps, (negative $n$ means rotate left)
- `d.reverse()` -> $O(n)$, reverses the deque in place.
- `d.clear()` -> $O(n)$ , removes all elements.
- `d.count(x)` -> $O(n)$, counts all occurences of $x$.
- `d.index(x)` -> $O(n)$, finds the index of $x$.
- `d.copy()` -> $O(n)$, shallow copy of the queue.
- `d[i]` -> $O(n)$, access by index (deque is not optimized for random access)
- `len(d)` -> $O(1)$, length of the deque.

### An important note
- `deque(maxlen=N)` creates a bounded `deque`, which is heavily used in sliding window approaches. If we add too much on the right, elements from the left starts popping.
```python
from collections import deque

d = deque(maxlen=3)
d.append(1); d.append(2); d.append(3); d.append(4)

print(d) # deque([2,3,4]). 1 got dropped off.
```
### Implementation of Queues using LinkedLists
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, val):
        newNode = Node(val)
        if not self.rear:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        self.size += 1

    def dequeue(self) -> int:
        if not self.rear:
            raise IndexError("deque from empty queue")
        val = self.front.val
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.size -= 1
        return val

    def peek(self) -> int:
        if not self.front:
            raise IndexError("peek from an empty queue")
        return self.front.val

    def is_empty(self) -> bool:
        return self.front is None
```

### Implementation of Queues using two stacks
```python
class QueueUsingStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, val) -> None:
        self.in_stack.append(val)

    def dequeue(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("dequeue from an empty queue")
        return self.out_stack.pop()

    def peek(self) -> bool:
        if len(self.in_stack) == 0:
            raise IndexError("empty queue")
        return self.in_stack[-1]:

    def is_empty(self) -> bool:
        return len(self.in_stack) == 0
```

### Implementation of Circular Queue
```python
class CircularQueue:
    def __init__(self, k):
        self.q = [None]*k
        self.capacity = k
        self.front = 0
        self.count = 0

    def enqueue(self,val) -> None:
        if self.count == self.capacity:
            raise OverflowError("queue is full")
        rear = (self.front + self.count) % self.capacity
        self.q[rear] = val
        count += 1

    def dequeue(self) -> int:
        if self.count == 0:
            raise IndexError("Empty Queue")
        val = self.q[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return val

    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count == self.capacity
```
## Double-ended Queues
### Introduction
- Double ended queues give us $O(1)$ functionality to append/pop on both left and right ends.
- Python's `collections.deque` is a double ended queue.
### Implementation using Doubly Linked Lists
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def append(self,val: int) -> None:
        newNode = Node(val)
        if not self.rear:
            self.front = self.rear = newNode
        else:
            newNode.prev = self.rear
            self.rear.next = newNode
            self.rear = newNode
        self.size += 1

    def appendleft(self, val: int) -> None:
        newNode = Node(val)
        if not self.rear:
            self.front = self.rear = newNode
        else:
            newNode.next = self.front
            self.front.prev = newNode
            self.front = newNode
        self.size += 1

    def pop(self) -> int:
        if not self.rear:
            raise IndexError("empty queue")
        val = self.rear.val
        self.rear = self.rear.prev
        if not self.rear:
            self.front = None
        else:
            self.rear.next = None
        self.size -= 1
        return val

    def popleft(self) -> int:
        if not self.rear:
            raise IndexError("empty queue")
        val = self.front.val
        self.front = self.front.next
        if not self.front:
            self.rear = None
        else:
            self.front.prev = None
        self.size -= 1
        return val

    def is_empty(self) -> bool:
        return self.size == 0

# all operations here are in O(1)
```

## Stack
### Stack Basics
- Stacks follows Last In, First Out (LIFO) protocol.
- We can generally use Python's default Lists as stacks.
- We may also use `collections.deque`
```python
stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop()) # pop and return the top element
print(stack[-1]) # peek
print(len(stack)) #size
print(not stack) #is_empty check
```

```python
# stacks using collections.deque
from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop()) # 3
print(stack[-1]) #peek
```
### Implementation using LinkedLists
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, val: int) -> None:
        newNode = Node(val)
        if not self.top:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.size += 1

    def pop(self) -> None:
        if not self.top:
            raise IndexError("Empty Stack")
        val = self.top.val
        self.top = self.top.next
        self.size -= 1
        return val

    def peek(self) -> int:
        if not self.top:
            raise IndexErro("Empty Stack")
        return self.top.val

    def is_empty(self) -> bool:
        return self.top is None
```
## Heaps / Priority Queues
### Basics
- Unlike LIFO or FIFO, PQs don't care about the insertion order but rather the priority order.
### `heapq` module
- `heapq` workd directly on python `list`, turning it into a binary heap in-place.
```python
import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)

print(heapq.heappop(heap)) # 1 -> smallest
print(heapq.heahpop(heap)) # 3
```
**heapq functions**
- `heapq.heappush(heap,x)` -> $O(\log n)$, push $x$ onto heap
- `heaq.heappop(heap)` -> $O(\log n)$, pop and return smallest item
- `heapq.heappushpop(heap,x)` -> $O(\log n)$, Push $x$ and then pop the smallest (more efficient than push + pop)
- `heapq.heapreplace(heap,x)` -> $O(\log n)$, Pop the smallest, and then push $x$
- `heapq.heapify(list)` -> $O(n)$, Convert an existing list into heap, in-place
- `heapq.nlargest(k, iterable)` -> $O(n \log k)$, returns the $k$ largest elements.
- `heapq.nsmallest(k, iterable)` -> $O(n \log k)$, returns the smallest $k$ elements.
- `heap[-1]` -> $O(1)$, Peek 

**max-heap trick**
- `heapq` only gives us min-heap, for max-heap, we can simply negate the values on the way in and way out.
```python
import heapq

heap = []
heapq.heappush(heap, -5)
heapq.heappush(heap, -1)
heapq.heappush(heap, -3)

print(-heapq.heappop(heap)) # 5 -> largest
print(-heapq.heappop(heap)) # 3 -> second largest
```
**Priority Queues with custom order (tuple)**
- tuples should be of the format `(priority, value)`
```python
import heapq

heap = []

heapq.heappush(heap, (2, "task x"))
heapq.heappush(heap, (1, "task l"))
heapq.heappush(heap, (3, "task c"))

print(heapq.heappop(heap)) # (1, "task l")
```

### Implementation of heaps from scratch
- A binary heap is stored as an array, where the children of index $i$ element are at $2i + 1$, and $2i + 2$, and its parent lives at $(i-1)//2$.
- `push` adds a value at the end and bubbles up (sift up).
- `pop` swaps the last value with the root and bubbles down (sift down).
- Both are $O(\log n)$, as the height of the tree is $\log n$. 
```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i-1)//2

    def _left(self, i):
        return 2*i+1

    def _right(self, i):
        return 2*i+2

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap)-1)

    def _sift_up(self, i):
        while i> 0 and self.heap[i] < self.heap[self._parent(i)]:
            p = self._parent(i)
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p

    def pop(self):
        if not self.heap:
            raise IndexError("Empty Heap")
        top = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return top

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            l, r = self._left(i), self._right(i)
            if l < n and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < n and self.heap[r] < self.heap[smallest]:
                smallest = r
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def peek(self):
        if not self.heap:
            raise IndexError("Empty Heap")
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0
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
**Note** - Inorder traversal of a BST gives a sorted array.
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

```python
# iterative traversal using explicit stack
def iterative_traversal(root: TreeNode) -> List[int]:
    result, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            result.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result
```
### Constructing a Binary Tree from preoder and inorder traversals
```python
# naive implementation
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(preorder, inorder):
    if not preoder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    mid = inorder.index(root_val)

    root.left = build_tree(preoder[1:mid+1],inorder[:mid] )
    root.right = build_tree(preorder[mid+1:], inorder[mid+1:])

    return root
```

```python
# optimal implementation
# we use a hashmap to lookup inorder index and used only pointers as opposed to copying the whole arrays

def build_tree(preorder, inorder):
    inorder_index = {val: i for i, val in enumerate(inorder)}
    self_preorder_idx = 0

    def helper(left, right):
        nonlocal self_preorder_idx
        if left > right:
            return None
        
        root_val = preorder[self_preorder_idx]
        root = TreeNode(root_val)
        self_preorder_idx += 1

        mid = inorder_index[root_val]

        root.left = helper(left, mid-1)
        root.right = helper(mid+1, right)

        return root
    
    return helper(0, len(preoder)-1)
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

### Diameter of a binary tree
- Maximum distance bw any two nodes, may or may not pass through root
```python
def diameter(root: TreeNode) -> int:
    result = 0
    def depth(root: TreeNode) -> int:
        nonlocal result
        if not root:
            return 0
        left = depth(root.left)
        right = depth(root.right)
        result = max(result, left+right)
        return 1 + max(left, right)
    depth(root)
    return result
```

### Check if balanced
```python
# balanced tree - diff bw left height and right height is bounded

```

## Binary Search Trees
### Basics
- For each node, `left` <= `node` <= `right`.

### Implementation from Scratch
```python
class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val: int) -> None:
        self.root = self._insert(self.root, val)

    def _insert(self, node: TreeNode, val: int) -> TreeNode:
        if node is None:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        return node

    def search(self, val: int) -> TreeNode:
        return self._search(self.root, val)

    def _search(self, node: TreeNode, val: int) -> TreeNode:
        if node is None or node.val == val:
            return node
        if val < node.val:
            return self._search(node.left, val)
        return self._serach(node.right, val)

    def delete(self, val: int) -> None:
        self.root = self._delete(self.root, val)

    def _delete(self, node: TreeNode, val: int) -> TreeNode:
        if node is None: return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        if val > node.val:
            node.right = self._delete(node.right, val)
        else: # found the match, now three cases
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            #when both children exist
            # find inorder successor (smallest in the right subtree)
            successor = node.right
            while successor.left:
                successor = successor.left
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)
        return node
```

### Validate a BST
```python
# check if a given tree is actually BST
def is_valid_bst(node: TreeNode, low = float('-inf'), high = float('inf')) -> bool:
    if not node: return True

    if not (low < node.val < high): return False

    return is_valid_bst(node.left, low, node.val) and is_valid_bst(node.right, node.val, high)
```

### Lowest Common Ancestor (LCA)
```python
def lca(root:TreeNode, p:int, q:int) -> TreeNode:
    if root is None or root.val == p or root.val == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right: return root

    return left if left else right
```


