# https://www.testdome.com/d/python-interview-questions/9

# 5. Binary Search Tree

import collections

class Node:

    def __init__(self, value, right, left):
        self.value = value
        self.right = right
        self.left = left

# Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    pass

n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 1))
