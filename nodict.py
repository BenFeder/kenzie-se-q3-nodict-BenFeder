#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Benjamin Feder'


class Node:
    def __init__(self, key, value=None):
        """Create key and value with a hash value for each Node"""
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
        """Create list of bucket lists, number of times given"""
        self.buckets = []
        for _ in range(num_buckets):
            self.buckets.append([])
        self.num_buckets = num_buckets

    def __repr__(self):
        """Return a string representing the NoDict contents."""
        # We want to show all the buckets vertically
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i,
                          bucket in enumerate(self.buckets)])

    def add(self, key, value):
        """Create new node in given bucket, by looping through each bucket
        to see if it belongs there, and delete it if it exists already
        and replace it, if not there already, just add it to the end"""
        new_node = Node(key, value)
        bucket_index = new_node.hash % self.num_buckets
        print(bucket_index)
        print(len(self.buckets))
        for node in self.buckets[bucket_index]:
            if node == new_node:
                self.buckets[bucket_index].remove(node)
                break
        self.buckets[bucket_index].append(new_node)

    def get(self, key):
        """Just like adding a new node, except it finds it and returns it"""
        node_to_find = Node(key)
        bucket_index = node_to_find.hash % self.num_buckets
        for node in self.buckets[bucket_index]:
            if node == node_to_find:
                return node.value
        raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        """Call the get method"""
        return self.get(key)

    def __setitem__(self, key, value):
        """Call the add method"""
        self.add(key, value)
