import unittest
from data_structures.arrays import array

# FILE: data_structures/test_arrays.py


class TestArray(unittest.TestCase):

    def test_append(self):
        array.append("test")
        self.assertEqual(array[-1], "test")

    def test_pop(self):
        array.append("test")
        item = array.pop()
        self.assertEqual(item, "test")
        self.assertNotIn("test", array)

    def test_slicing(self):
        array.extend(["a", "b", "c", "d"])
        sliced = array[1:3]
        self.assertEqual(sliced, ["b", "c"])

    def test_indexing(self):
        array.extend(["a", "b", "c", "d"])
        self.assertEqual(array[2], "c")

if __name__ == "__main__":
    unittest.main()