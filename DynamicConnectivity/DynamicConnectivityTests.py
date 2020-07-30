import unittest

from QuickFind import QuickFind


class TestDynamicConnectivity(unittest.TestCase):

    def test_find_unconnected(self):
        quick_find = QuickFind(10)
        self.assertFalse(quick_find.find(0, 1))

    # Test connected two nodes are connected successfully
    def test_find_connected_union(self):
        quick_find = QuickFind(10)
        quick_find.union(0, 1)
        self.assertTrue(quick_find.find(0, 1))

    # Test connected three nodes are connected successfully
    def test_find_connected_union_trio(self):
        quick_find = QuickFind(10)
        quick_find.union(0, 1)
        quick_find.union(0, 2)

        self.assertTrue(quick_find.find(0, 1))
        self.assertTrue(quick_find.find(0, 2))
        self.assertTrue(quick_find.find(1, 2))


if __name__ == '__main__':
    unittest.main()
