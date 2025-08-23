"""
Essential Data Structures for DSA Practice

Simple implementations of the most commonly used data structures.
"""

from collections import deque
from typing import Optional, List


class ListNode:
    """Singly Linked List Node - commonly used in LeetCode style problems"""

    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        """String representation for easy debugging"""
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
            if len(result) > 10:  # Prevent infinite loops
                result.append("...")
                break
        return " -> ".join(result)

    @classmethod
    def from_list(cls, arr: List[int]) -> Optional['ListNode']:
        """Create linked list from Python list"""
        if not arr:
            return None

        head = cls(arr[0])
        current = head
        for val in arr[1:]:
            current.next = cls(val)
            current = current.next
        return head

    def to_list(self) -> List[int]:
        """Convert linked list to Python list"""
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
            if len(result) > 1000:  # Safety check
                break
        return result


class TreeNode:
    """Binary Tree Node - commonly used in tree problems"""

    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: List[Optional[int]]) -> Optional['TreeNode']:
        """Create binary tree from level-order list (LeetCode style)"""
        if not arr or arr[0] is None:
            return None

        root = cls(arr[0])
        queue = deque([root])
        i = 1

        while queue and i < len(arr):
            node = queue.popleft()

            # Left child
            if i < len(arr) and arr[i] is not None:
                node.left = cls(arr[i])
                queue.append(node.left)
            i += 1

            # Right child
            if i < len(arr) and arr[i] is not None:
                node.right = cls(arr[i])
                queue.append(node.right)
            i += 1

        return root
