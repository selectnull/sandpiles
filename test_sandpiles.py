import unittest
from sandpiles import Sandpile


class TestInit(unittest.TestCase):
    def test_no_arguments_raises_valueerror(self):
        with self.assertRaises(ValueError):
            Sandpile()

    def test_size_and_no_data_inits_data_with_zeros(self):
        for x in Sandpile(size=3).data:
            for y in x:
                self.assertEqual(y, 0)

    def test_data_sets_correct_size(self):
        assert Sandpile(data=[ [0, 1], [0, 1] ]).size == 2

    def test_exception_is_raised_if_size_does_not_match_data(self):
        with self.assertRaises(ValueError):
            Sandpile(size=3, data=[ [0, 1], [0, 1] ])

    def test_size_0_raises_valueerror(self):
        with self.assertRaises(ValueError):
            Sandpile(size=0)

    def test_negative_size_raises_valueerror(self):
        with self.assertRaises(ValueError):
            Sandpile(size=-1)


class TestDataValidity(unittest.TestCase):
    def test_is_valid(self):
        self.assertTrue(Sandpile(data=[ [0, 1], [0, 1] ]).is_valid())

    def test_4_is_not_valid_value(self):
        self.assertFalse(Sandpile(data=[ [0, 1], [0, 4] ]).is_valid())

    def test_values_must_be_ints(self):
        self.assertFalse(Sandpile(data=[ [0, '1'], [0, 4] ]).is_valid())


class TestNeighbours(unittest.TestCase):
    def setUp(self):
        self.s = Sandpile(size=3)

    def test_top_left(self):
        self.assertEqual(self.s.neighbours(0, 0), [ (0, 1), (1, 0) ])

    def test_top_middle(self):
        self.assertEqual(self.s.neighbours(0, 1), [ (0, 0), (0, 2), (1, 1) ])

    def test_top_right(self):
        self.assertEqual(self.s.neighbours(0, 2), [ (0, 1), (1, 2) ])

    def test_middle_left(self):
        self.assertEqual(self.s.neighbours(1, 0), [ (0, 0), (1, 1), (2, 0) ])

    def test_middle_middle(self):
        self.assertEqual(self.s.neighbours(1, 1), [ (0, 1), (1, 0), (1, 2), (2, 1) ])

    def test_middle_right(self):
        self.assertEqual(self.s.neighbours(1, 2), [ (0, 2), (1, 1), (2, 2) ])

    def test_bottom_left(self):
        self.assertEqual(self.s.neighbours(2, 0), [ (1, 0), (2, 1) ])

    def test_bottom_middle(self):
        self.assertEqual(self.s.neighbours(2, 1), [ (1, 1), (2, 0), (2, 2) ])

    def test_bottom_right(self):
        self.assertEqual(self.s.neighbours(2, 2), [ (1, 2), (2, 1) ])


class TestBehaviour(unittest.TestCase):
    def test_topple(self):
        s0 = [ [4, 3, 3], [3, 1, 2], [0, 2, 3] ]
        s1 = [ [0, 4, 3], [4, 1, 2], [0, 2, 3] ]
        s2 = [ [2, 0, 4], [0, 3, 2], [1, 2, 3] ]
        s3 = [ [2, 1, 0], [0, 3, 3], [1, 2, 3] ]

        a = Sandpile(data=s1)
        steps = a.topple()
        self.assertEqual(a.data, s3)
