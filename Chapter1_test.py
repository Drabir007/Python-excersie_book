from unittest import TestCase
from Chapter1 import s


class TestChapter1(TestCase):
    def test_summation(self):
        self.assertEqual(3, s(1, 2), "1+2=3")