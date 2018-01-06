from context import util
import unittest


class TestUtilClasses(unittest.TestCase):

    def test_pair_initialization(self):
        pair = Pair(50, -30)
        self.assertEquals(pair.first, 50)
        self.assertEquals(pair.second, -30)

    def test_pair_swap(self):
        pair = Pair(20, 100)
        pair.swap()
        self.assertEquals(pair.first, 100)
        self.assertEquals(pair.second, 20)

