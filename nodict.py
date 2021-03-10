#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Benjamin Feder'


class Node:
    def __init__(self, key, value=None):
        self.hash = hash(key)
        self.key = key
        self.value = value

    def __repr__(self):
        """returns a string based on key an value of class Node instance"""
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """Checks to see if two keys are equal"""
        if isinstance(other, Node):
            if self.key == other.key:
                return True
        return False


class NoDict:
    def __init__(self, num_buckets=10):
        self.buckets = None
        # Your code here

    def __repr__(self):
        """Return a string representing the NoDict contents."""
        # We want to show all the buckets vertically
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        # Your code here
        return

    def get(self, key):
        # Your code here
        return

    def __getitem__(self, key):
        # Your code here
        return

    def __setitem__(self, key, value):
        # Your code here
        return
