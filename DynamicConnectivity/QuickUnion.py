# Lazy algorithm for solving dynamic connectivity problem
# Data structure
#   Integer array id[] of size N
#   Interpretation - array representing set of trees, each entry in array contains reference to parent
#    id[i] is parent of i
# root of i is id[id[i]] - keep going until the value doesn't change


class QuickUnion:

    # n being the number of nodes
    def __init__(self, n):
        self.id = []
        for x in range(n):
            self.id.append(x)

    # Given an id, i, find the root node
    def root(self, i):
        # While the node i and its root are not equal, follow the tree to its root
        while i != self.id[i]:
            i = self.id[i]
        return i

    # Given two ids, return true if they are connected, false if not
    # Two nodes are connected if their root nodes are the same
    def find(self, first_id, second_id):
        if self.root(first_id) == self.root(second_id):
            return True
        else:
            return False

    # Given two nodes, connect them
    # Two nodes are connected by setting id of second_id's root to the id of first_id's root
    def union(self, first_id, second_id):
        first_root = self.root(first_id)
        second_root = self.root(second_id)
        self.id[second_id] = first_root

