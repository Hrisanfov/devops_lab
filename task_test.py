from unittest import TestCase

import task6


class TestPrime(TestCase):

    def test_func(self):
        """Test for func"""
        self.assertEquals(task6.func([89, 90, 78, 93, 80], [90, 91, 85, 88, 86]), [89.5, 90.5, 81.5, 90.5, 83.0])



