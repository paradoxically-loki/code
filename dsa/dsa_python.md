# DSA Notes in Python

## Linked Lists
### Basic Structure
```python
# linked lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def insert_at_end(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def delete_node_by_value(self, val):
        current = self.head

        if current and current.data == val:
            self.head = current.next
            current.next = None

        prev = Node
        while current and current.data != val:
            prev = current
            current = current.next

        if current is None: #not found in the entire list
            return

        prev.next = current.next # if we have found it
        current.next = None

    def printLL(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()

ll.insert_at_beginning(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.delete_node_by_value(6)
ll.printLL()    
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

