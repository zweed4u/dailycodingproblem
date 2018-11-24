#!/usr/bin/python3
"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""

class Node:
    def __init__(self):
        # eg. 0b1001 ^ 0b0110 = 15
        # 0b1001 ^ 0b1001 = 0
        self.both = None

    def set(self, previous_node=0, next_node=0):
        self.both = previous_node ^ next_node  # XOR of next node and previous node


class XORLinkedList:
    def __init__(self):
        pass

    def add(self, element):
        pass  # adds an element to the end of the linkedlist

    def get(self, index):
        pass  # returns the node at the index


n1 = Node()
n2 = Node()
n3 = Node()

# Split into set method so that there isn't Name error undefined if prev and next nodes are in constructor
n1.set(0, n2)
n2.set(n1, n3)
n3.set(n2, 0)

xll = XORLinkedList()
