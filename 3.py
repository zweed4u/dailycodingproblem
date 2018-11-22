#!/usr/bin/python3
"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
import json


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    binary_tree_as_dict = {node.val: {'left': [], 'right': []}}
    
    current_node = node
    try:
        while current_node.val is not None:
            binary_tree_as_dict[node.val]['left'].append(current_node.left)
            binary_tree_as_dict[node.val]['right'].append(current_node.right)
            current_node = current_node.left
    except:
        pass

    current_node = node.right
    try:
        while current_node.val is not None:
            binary_tree_as_dict[node.val]['left'].append(current_node.left)
            binary_tree_as_dict[node.val]['right'].append(current_node.right)
            current_node = current_node.right
    except:
        pass

    for index, n in enumerate(binary_tree_as_dict[node.val]['left']):
        if isinstance(n, Node):
            binary_tree_as_dict[node.val]['left'][index] = n.val

    for index, n in enumerate(binary_tree_as_dict[node.val]['right']):
        if isinstance(n, Node):
            binary_tree_as_dict[node.val]['right'][index] = n.val

    print(json.dumps(binary_tree_as_dict, indent=4))

def deserialize(serialized_node):
    pass

#        1
#   2        3
# 4   5        6
#7
node_7 = Node('left.left.left', None, None)
node_4 = Node('left.left', node_7, None)
node_6 = Node('right.right', None, None)
node_5 = Node('left.right', None, None)
node_3 = Node('right', None, node_6)
node_2 = Node('left', node_4, node_5)
node_1 = Node('root', node_2, node_3)
serialize(node_1)
#assert deserialize(serialize(node_1)).left.left.val == 'left.left'
