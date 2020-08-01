# Lazy algorithm for solving dynamic connectivity problem
# Modified quick union - link root of smaller tree t o root of larger tree
# Data structure
#   Integer array id[] of size N
#   Interpretation - array representing set of trees, each entry in array contains reference to parent
#    id[i] is parent of i
# root of i is id[id[i]] - keep going until the value doesn't change

from QuickUnion import QuickUnion


class WeightedQuickUnion(QuickUnion):

    # n being the number of nodes
    # sz being the size of the tree
    def __init__(self, n):
        super().__init__(n)
        self.sz = []
        for x in range(n):
            # Set the size of each tree initially to 1
            self.sz.append(1)

    # Given two nodes, connect them
    # Two nodes are connected by setting id of the smallest root to the id of the largest root
    def union(self, first_id, second_id):
        first_root = self.root(first_id)
        second_root = self.root(second_id)
        # If first_id has a greater sized tree, set second_id root to first_id root, and update the size of first_id
        if self.sz[first_id] >= self.sz[second_root]:
            self.id[second_id] = first_root
            self.sz[first_id] += self.sz[second_id]
        else:
            self.id[first_id] = second_root
            self.sz[second_id] += self.sz[first_id]


