# Quick find algorithm for solving the dynamic connectivity problem
# Data structure:
#   Integer array id of size n
#   p and q connected iff they have the same id


class QuickFind:

    # n being the number of nodes
    def __init__(self, n):
        self.id = []
        for x in range(n):
            self.id.append(x)

    # Given two ids, return true if they are connected (connected if their array id is the same)
    def find(self, first_id, second_id):
        if self.id[first_id] == self.id[second_id]:
            return True
        else:
            return False

    # Given two ids, connect this pair (change all entries of id whose id = id[second_id] to id[first_id]
    def union(self, first_id, second_id):
        id_to_change = self.id[second_id]
        for x in self.id:
            if self.id[x] == id_to_change:
                self.id[x] = self.id[first_id]

