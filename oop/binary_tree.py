# https://www.testdome.com/d/python-interview-questions/9

# 5. Binary Search Tree

import collections

class Node:
    def __init__(self, value, right, left):
        self.value = value
        self.right = right
        self.left = left
       
    def __str__(self):
        return f'Node {self.value}'

# Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    if root.value == value:
        return True
    elif root.value < value:
        if root.right is None:
            return False
        else:
            return contains(root.right, value)

    else:
        if root.left is None:
            return False
        else:
            return contains(root.left, value)

n1 = Node(value=1, left=None, right=None)
n4 = Node(value=4, left=None, right=None)
n7 = Node(value=7, left=None, right=None)
n13 = Node(value=13, left=None, right=None)
n14 = Node(value=14, left=n13, right=None)
n6 = Node(value=6, left=n4, right=n7)
n3 = Node(value=3, left=n1, right=n6)
n10 = Node(value=10, left=None, right=n14)
n8 = Node(value=8, left=n13, right=n10)
        
print(contains(n8, 1))
        

