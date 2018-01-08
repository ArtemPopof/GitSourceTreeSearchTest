from unittest import TestCase

from util import Pair


class TestUtilClasses(TestCase):
    def test_pair_initialization(self):
        pair = Pair(50, -30)

        self.assertEqual(pair.first, 50)
        self.assertEqual(pair.second, -30)

    def test_pair_swap(self):
        pair = Pair(20, 100)
        pair.swap()

        self.assertEqual(pair.first, 100)
        self.assertEqual(pair.second, 20)
