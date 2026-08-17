# DSA Notes in Python

## List of Contents
- [Basics](#basics)
   - [Dictionary](#dictionary)
   - [Sets](#sets)
- [Arrays](#arrays)
   - [Static Arrays](#static-arrays)
   - [Dynamic Arrays](#dynamic-arrays)
   - [Implementation of a Dynamic Array](#implementation-of-a-dynamic-array)
- [Strings](#strings)
    - [Basics of Strings](#basics-of-strings)
    - [Common Built-in Methods](#common-built-in-methods)
- [Sorting](#sorting)
    - [Time Complexities](#time-complexities)
    - [Comparison Based Algorithms](#comparison-based-algorithms)
    - [Non-Comparison Based Algorithms](#non-comparison-based-algorithms)
- [Linked Lists](#linked-lists)
   - [Basic Structure](#basic-structure)
   - [Reversing a Linked List](#reversing-a-linked-list)
   - [Detecting Cycle](#detecting-cycle)
- [Queue](#queue)
   - [`deque` functions](#some-important-featuresfunctions-on-deque)
   - [Queue using Linked Lists](#implementation-of-queues-using-linkedlists)
   - [Queue using two Stacks](#implementation-of-queues-using-two-stacks)
   - [Circular Queue](#implementation-of-circular-queue)
- [Double Ended Queue](#double-ended-queues)
- [Stacks](#stack)
- [Heaps/Priority Queue](#heaps--priority-queues)
   - [`heapq` module](#heapq-module)
   - [Implementation from scratch](#implementation-of-heaps-from-scratch)
- [Binary Trees](#binary-trees)
   - [Traversals (pre/in/post/BFS/iterative)](#binary-trees-traversal)
   - [Build from Preorder + Inorder](#constructing-a-binary-tree-from-preoder-and-inorder-traversals)
   - [Height / Node Count / Identical / Subtree](#height-of-a-binary-tree)
   - [Diameter](#diameter-of-a-binary-tree)
   - [Check if Balanced](#check-if-balanced)- [Binary Search Trees](#binary-search-trees)
   - [Insert / Search / Delete](#implementation-from-scratch)
   - [Validate a BST](#validate-a-bst)
   - [Lowest Common Ancestor](#lowest-common-ancestor-lca)
- [Graphs](#graphs)
    - [Representation (Adjacency List/Matrix, Edge List)](#representation)
    - [Traversals (DFS/BFS)](#traversals)
    - [Cycle Detection (Directed/Undirected)](#common-algorithms)
    - [Topological Sort / Kahn's Algorithm](#topological-sort-dags-only)
    - [Connected Components](#number-of-connected-components)
    - [Dijkstra's Algorithm](#dijkstras-algorithm-only-for-non-negative-weights)


## Basics
### Dictionary
```python
d = {'a': 1, 'b': 2}
```
**Common Operations**

| Operation | Syntax | Average case | Worst case |
|---|---|---|---|
| Access value | `d['a']` or `d.get('a')` | O(1) | O(n) |
| Insert / update | `d['c'] = 3` | O(1) | O(n) |
| Delete | `del d['a']` or `d.pop('a')` | O(1) | O(n) |
| Check key exists | `'a' in d` | O(1) | O(n) |
| Get with default | `d.get('x', default)` | O(1) | O(n) |
| Get all keys | `d.keys()` | O(1) to get view, O(n) to iterate | — |
| Get all values | `d.values()` | O(1) to get view, O(n) to iterate | — |
| Get all items | `d.items()` | O(1) to get view, O(n) to iterate | — |
| Length | `len(d)` | O(1) | — |
| Pop last added item | `d.popitem()` | O(1) | — |
| Merge | `d.update(other)` | O(len(other)) | — |
| Copy | `d.copy()` | O(n) | — |
| Clear | `d.clear()` | O(1)* | — |
| setdefault | `d.setdefault('x', [])` | O(1) | O(n) |

**Dict Comprehension in frequency counting**

```python
# vanilla dictionary
freq = {}
for x in arr:
    freq[x] = freq.get(x,0) + 1

# with defaultdict
from collections import defaultdict
freq = defaultdict(int) # int as factory means missing keys default to int() == 0
for x in arr:
    freq[x] += 1

# counter (especially for frequency calc)
from collections import Counter
freq = Counter(arr)
```

```python
c = Counter("aabbbc")
print(c) # Counter({'b': 3, 'a': 2, 'c': 1})
print(c.most_common(2)) # [('b', 3), ('a', 2)]
```
### Sets
```python
s = {1,2,3} # initilisation with values
s = set() # empty initialisation
```

**Common Operations**

| Operation | Syntax | Average case | Worst case |
|---|---|---|---|
| Add element | `s.add(4)` | O(1) | O(n) |
| Remove element | `s.remove(4)` (errors if missing) | O(1) | O(n) |
| Discard element | `s.discard(4)` (no error if missing) | O(1) | O(n) |
| Check membership | `4 in s` | O(1) | O(n) |
| Length | `len(s)` | O(1) | ------ |
| Pop arbitrary (random) | `s.pop()` | O(1) | ------ |
| Union | `s1 \| s2` | O(len(s1) + len(s2)) | ------ |
| Intersection | `s1 & s2` | O(min(len(s1), len(s2))) | ------ |
| Difference | `s1 - s2` | O(len(s1)) | ------ |
| Symmetric difference | `s1 ^ s2` | O(len(s1) + len(s2)) | ------ |
| Subset check | `s1 <= s2` | O(len(s1)) | ------ |
| Copy | `s.copy()` | O(n) | ------ |


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
- Inserting at the front is anyway $O(n)$ in both cases, as we have to shift the entire list.

### Some important features/functions for Arrays

| Category | Operation | Time Complexity | Notes |
|---|---|---|---|
| **Access** | `arr[i]` | O(1) | Direct index access |
| | `len(arr)` | O(1) | Python lists track length, not counted each time |
| | `arr[a:b]` | O(k) | Slicing creates a new list, doesn't view the original |
| **Adding Elements** | `arr.append(x)` | O(1) amortized | Adds at the end |
| | `arr.extend(iterable)` | O(k) amortized | Adds each element of another iterable |
| | `arr.insert(i, x)` | O(n) | Everything from the index onwards needs to be shifted |
| **Removing Elements** | `arr.pop()` | O(1) | Removes from the end, no shift needed |
| | `arr.pop(i)` | O(n) | Everything past the index needs to be shifted |
| | `arr.remove(x)` | O(n) | Searches for the first match, then shifts |
| | `del arr[i]` | O(n) | Same cost as pop |
| | `arr.clear()` | O(n) | — |
| **Search** | `x in arr` | O(n) | Linear search |
| | `arr.index(x)` | O(n) | Returns position |
| | `arr.count(x)` | O(n) | — |
| **Reordering** | `arr.sort()` | O(n log n) | TimSort under the hood, stable |
| | `sorted(arr)` | O(n log n) | Returns a new list, instead of in-place sorting |
| | `arr.reverse()` | O(n) | — |
| | `arr[::-1]` | O(n) | Same idea, but returns a new list |
| **Combining** | `arr1 + arr2` | O(n+m) | Creates a new list |
| | `arr * k` | O(nk) | — |

**Note**: `pop(0)` and `insert(0, x)` are O(n), not O(1), since the whole list has to shift.
### Implementation of a Dynamic Array
```python
class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0]*self.capacity

    def get(self, i: int) -> int:
        if not 0 <= i <= self.length-1:
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
        if self.length == 0:
            raise IndexError('pop from empty array')
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

## Strings
### Basics of Strings
- Strings are immutable, so every modification on them creates a new string.
- So, `s += char` in a loop is $O(n^2)$.
```python
s = "hello"
s[0] = 'H' # TypeError: Strings don't support item assignment
```
**Fix for building strings in a loop**
```python
# bad method - O(n^2)
result = ""
for c in some_list:
    result += c

# good method - O(n)
result = []
for c in some_list:
    result.append(c)
result = "".join(result)
```

**Access and Slicing**
```python
s = "hello world"

s[0]        # 'h', O(1)
s[-1]       # 'd', O(1)
s[2:5]      # 'llo', O(k), slicing creates a new string
s[::-1]     # reverses the string, O(n)
s[::2]      # 'hlowrd', every second character 
len(s)      # length, O(1)
```
### Common Built-in Methods
**Case and Formatting**
```python
s = "hello"
s.upper()         # "HELLO"
s.lower()         # "hello"
s.title()         # "Hello World"
s.capitalize()    # "Hello world"
s.swapcase()      # swap upper/lower
```

**Whitespace and cleaning**
```python
s.strip()           # removes leading and trailing whitespaces
s.strip('xyz')      # removes leading and trailing chars from the given set
s.lstrip()          # removes leading whitespaces
s.rstrip()          # removes trailing whitespaces
```

**Searching**
```python
s.find('lo')         # finds first occurence, returns -1 if not found
s.rfind('lo')        # finds first occurence from the end, returns -1 if not found
s.index('lo')        # same as find, but gives ValueError if not found
'lo' in s            # O(n), membership check
s.count('l')         # counts non-overlapping occurences, O(n)
s.startswith('hel')  # O(k)
s.endswith('rld')    # O(k)
```

**Splitting and Joining**
```python
s = 'hello world'

s.split()                   # ['hello', 'world'], splits on white space
s.split(',')                # splits on a specified delimiter
s.split(',', 1)             # maxsplit, only splits once
s.rsplit(',', 1)            # splits from the right
s.splitlines()              # splits on line breaks
','.join(['a', 'b', 'c'])   # 'a,b,c', O(n)
```
`s.split()` also handles multiple spaces, leading/trailing whitespaces pretty cleanly.

**Replacing**
```python
s.replace('l', 'L')       # replaces all occurences, O(n)
s.replace('l', 'L', 1)    # replace only the first occurence
```

**Checking character types**
```python
c.isalpha()         # is alphabet
c.isdigit()         # is digit
c.isalnum()         # is digit or alphabet
c.isupper()         # is uppercase
c.islower()         # is lowercase
c.isspace()         # is whitespace
```

**Padding and Alignment**
```python
s.zfill(5)          # '00042' for '42', pads with zeros on the left
s.ljust(10, '*')    # left-justify, pad right
s.rjust(10, '*')    # right-justify, pad left
s.center(10, '*')   # center with padding
```

### Character <-> ASCII Coversion
```python
ord('a')   # 97, characted to ASCII/Unicode code point
chr(97)    # 'a', code point to character

# common pattern: map 'a'-'z' to indices 0-25
index = ord(ch) - ord('a')
letter = chr(index + ord('a'))
```

### String <-> list conversion (in-place-style manipulation)
```python
s = 'hello'
chars = list(s)     # ['h', 'e', 'l', 'l', 'o']
chars[0] = 'H'
s = ''.join(chars)  # 'Hello'
```

### String Comparison
```python
"abc" == "abc"          # True, value comparison
"abc" < "abd"           # True, lexicographic comparison, character by character

sorted("cab")           # ['a', 'b', 'c'], returns a list, not a string
''.join(sorted("cab"))  # 'abc'
```

## Sorting
### Time Complexities

| Algorithm | Best | Average | Worst | Space | Stable? |
|---|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(n+k) | Yes |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n+k) | Yes |
| Bucket Sort | O(n+k) | O(n+k) | O(n²) | O(n) | Yes (depends on inner sort) |
| Tim Sort (Python's `sort()`) | O(n) | O(n log n) | O(n log n) | O(n) | Yes |

**Stability:** If two elements are same, their relative order remains same.

### Comparison based Algorithms
#### Bubble Sort
- Repeatedly swaps adjacent elements if they're out of order. 
- Each pass "bubbles" the largest unsorted element to its corrent order.
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped if False:
            break #already sorted, break early
    return arr
```

#### Selection Sort
- Repeatedly finds the minimum of the unsorted portion and swaps it into place.
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

#### Insertion Sort
- Builds the sorted array, one element at a time.
- Inserts each new element into its correct position among the already-sorted part.
```python
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
```

#### Merge Sort
- DnC: Divide the array into halves, sort them and merge back
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(left[j:])

    return result
```

#### Quick Sort
- DnC: Pick a pivot, parition the array such that smaller elements are to the left of the pivot and the rest are on the right.
- Recurse on each step.
```python
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr)-1
    if low < high:
        pivot_idx = partition(arr,low,high)
        quick_sort(arr,low,pivot_idx-1)
        quick_sort(arr,pivot_idx+1,high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
```
#### Heap Sort
- Builds a max-heap from the array, then repeatedly extract the max and place it at the end.
```python
def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

def heapify(arr, n, i):
    largest = i
    left, right = 2*i + 1, 2*2 + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

### Non-comparison based Algorithms

#### Counting Sort
- Counts the occurences of each value and then reconstructs the sorted array
```python
def counting_sort(arr):
    if not arr: return arr

    max_val = max(arr)
    count = [0]*(max_val + 1)

    for x in arr:
        count[x] += 1

    result = []
    for val, c in enumerate(count):
        result.extend([val]*c)
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

| Operation | Time Complexity | Notes |
|---|---|---|
| `d.append(4)` | O(1) | Appends to the right |
| `d.appendleft(0)` | O(1) | Appends to the left |
| `d.pop()` | O(1) | Removes and returns the rightmost element |
| `d.popleft()` | O(1) | Removes and returns the leftmost element |
| `d.extend(iterable)` | O(k) | Appends multiple elements to the right |
| `d.extendleft(iterable)` | O(k) | Appends multiple elements to the left (in reverse order) |
| `d.insert(i, x)` | O(n) | Inserts x at index i |
| `d.remove(x)` | O(n) | Removes the first occurrence of x |
| `d.rotate(n)` | O(k) | Rotates by n steps (negative n means rotate left) |
| `d.reverse()` | O(n) | Reverses the deque in place |
| `d.clear()` | O(n) | Removes all elements |
| `d.count(x)` | O(n) | Counts all occurrences of x |
| `d.index(x)` | O(n) | Finds the index of x |
| `d.copy()` | O(n) | Shallow copy of the deque |
| `d[i]` | O(n) | Access by index, deque is not optimized for random access |
| `len(d)` | O(1) | Length of the deque |

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
            raise IndexError("dequeue from an empty queue")
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

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("peek from an empty queue")
        return self.out_stack[-1]

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
        self.count += 1

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
            raise IndexError("Empty Stack")
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
print(heapq.heappop(heap)) # 3
```
**heapq functions**

| Function | Time Complexity | Notes |
|---|---|---|
| `heapq.heappush(heap, x)` | $O(\log n)$ | Push $x$ onto heap |
| `heapq.heappop(heap)` | $O(\log n)$ | Pop and return smallest item |
| `heapq.heappushpop(heap, x)` | $O(\log n)$ | Push $x$ and then pop the smallest (more efficient than push + pop) |
| `heapq.heapreplace(heap, x)` | $O(\log n)$ | Pop the smallest, and then push $x$ |
| `heapq.heapify(list)` | $O(n)$ | Convert an existing list into a heap, in-place |
| `heapq.nlargest(k, iterable)` | $O(n \log k)$ | Returns the $k$ largest elements |
| `heapq.nsmallest(k, iterable)` | $O(n \log k)$ | Returns the smallest $k$ elements |
| `heap[0]` | $O(1)$ | Peek (smallest element sits at index 0, not -1) |

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
def postorder_dfs(root: TreeNode) -> None:
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
# iterative inorder traversal using explicit stack
def iterative_traversal(root: TreeNode) -> List[int]:
    result, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.data)
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
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    mid = inorder.index(root_val)

    root.left = build_tree(preorder[1:mid+1], inorder[:mid])
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
    
    return helper(0, len(preorder)-1)
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

    if not subRoot: return True
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
- Balanced tree: for every node, the height difference between left and right subtrees is at most 1.
- Naive approach recomputes height at every node -> $O(n^2)$. Better: compute height and check balance in a single bottom-up pass -> $O(n)$.
```python
def is_balanced(root: TreeNode) -> bool:
    def height(node: TreeNode) -> int:
        if not node:
            return 0
        left = height(node.left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) != -1
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
        return self._search(node.right, val)

    def delete(self, val: int) -> None:
        self.root = self._delete(self.root, val)

    def _delete(self, node: TreeNode, val: int) -> TreeNode:
        if node is None: return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
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

## Graphs
### Basics
- Graphs is a set of nodes (or vertices) connected via edges.
- No hierarchy, unlike trees.
- Types of Graphs:
    - Directed
    - Undirected
    - Weighted
    - Unweighted
    - Cyclic
    - Acyclic
    - Connected
    - Sparse vs Dense
### Representation
#### Adjacency List
- A dictionary mapping each node to a list of  its neighbors. Efficient for sparse graphs.
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```
- For weighted graphs, we store `(neighbor, weight)` pairs.
```python
graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('A', 4), ('D', 2)],
    'C': [('A', 1), ('D', 5)],
    'D': [('B', 2), ('C', 5)]
}
```
#### Adjacency Matrix
- A 2d array, where `matrix[i][j] = 1` if there is an edge between `i` and `j`.
```python
# 4 nodes: 0, 1, 2, 3
matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]
```
#### Edge List
- Just a flat list of edges. (rarely used for traversal but common way of input in Qs)
```python
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]
```

#### Building an adjacency list from edge list
```python
from collections import defaultdict
def build_adj_list(edges: List, directed = False) -> dict:
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph

# defaultdict here handles the case when the node is not present in graph

def build_adj_list(edges: List, directed: bool = False) -> dict:
    graph = {}
    for u,v in edges:
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
        if not directed:
            if v not in graph:
                graph[v] = []
            graph[v].append(u)
    return graph
```
### Traversals
#### DFS (Recursive)
```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    result = [node]
    for neighbor in graph[node]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result
```

#### DFS (Iterative using Stack)
```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return result
```

#### BFS (always iterative, uses Queue)
```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    q = deque([start])
    result = []
    while q:
        node = q.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return result
```

### Common Algorithms
#### Detect a Cycle (Undirected Graph)
```python
def detect_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None): return True
    return False
```

#### Detect a Cycle (Directed Graph)
```python
def detect_cycle_directed(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}

    def dfs(node):
        color[node] = GRAY
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK
        return False

    for node in graph:
        if color[node] == WHITE:
            if dfs(node): return True
    return False
```

#### Topological Sort (DAGs Only)
```python
def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node) # add after all descendants are processed

    for node in graph:
        if node not in visited:
            dfs(node)
    
    return stack[::-1]
```

#### Kahn's Algorithms (BFS Alternative, detects cycle also)
```python
from collections import deque, defaultdict

def topological_sort_kahn(graph, nodes):
    in_degree = {n: 0 for n in nodes}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    q = deque([n for n in nodes if in_degree[n] == 0])
    result = []

    while q:
        node = q.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)

    if len(result) != len(nodes):
        return None # cycle detected, no valid topological order
    return result
```

#### Number of connected Components
```python
def count_components(graph,nodes):
    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    for node in nodes:
        if node not in visited:
            dfs(node)
            count += 1
    return count
```

#### Dijkstra's Algorithm (only for non-negative weights)
```python
import heapq

def dijkstra(graph, start):
    dist = {start:0}
    heap = [(0, start)]

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist.get(node, float('inf')):
            continue
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return dist
```