# Simple DSA Python Environment

A minimal, college-style environment for Data Structures and Algorithms practice in Python.

## 🚀 Quick Start

1. **Write your algorithm** in any topic folder
2. **Run directly**: `python filename.py`
3. **That's it!** No complex setup needed.

## 📁 Project Structure

```
DSA_PYTHON/
├── README.md                 # This file
├── utils/                   # Essential data structures only
│   ├── __init__.py
│   └── data_structures.py   # ListNode, TreeNode
├── templates/               # Simple template
│   └── algorithm_template.py
└── topics/                  # Organized by DSA topics
    ├── arrays/
    ├── linked_lists/
    ├── stacks_queues/
    ├── trees/
    ├── graphs/
    ├── sorting/
    ├── searching/
    ├── dynamic_programming/
    ├── greedy/
    ├── backtracking/
    ├── math/
    └── strings/
```

## 📖 How to Use

### 1. Copy the template
```bash
cp templates/algorithm_template.py topics/arrays/two_sum.py
```

### 2. Edit and implement
```python
from utils import ListNode, TreeNode  # if needed

def solve(input_data):
    # Your algorithm here
    return result
```

### 3. Run directly
```bash
python topics/arrays/two_sum.py
```

## 🛠️ Available Utilities

- **ListNode**: For linked list problems
- **TreeNode**: For binary tree problems
- Both include helper methods like `from_list()` for easy testing

## 📝 Example

```python
#!/usr/bin/env python3
from utils import ListNode

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    return prev

if __name__ == "__main__":
    # Test
    head = ListNode.from_list([1, 2, 3, 4, 5])
    reversed_head = reverse_list(head)
    print(reversed_head)  # 5 -> 4 -> 3 -> 2 -> 1
```

**College-style simplicity**: Just write your algorithm and run it! 🎯
