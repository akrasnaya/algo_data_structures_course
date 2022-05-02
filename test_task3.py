import unittest

from task3 import DynArray


def create_array_to_test(size):
    da = DynArray()
    for i in range(size):
        da.append(i)
    return da


class TestDynArray(unittest.TestCase):
    def insert_invalid_position(self):
        data = create_array_to_test(5)
        self.assertRaises(IndexError, data.insert(-1, 9))
        self.assertRaises(IndexError, data.insert(9, 9))

    def insert_same_buffer(self):
        data = create_array_to_test(5)
        data.insert(2, 10)
        self.assertListEqual([element for element in data], [0, 1, 10, 2, 3, 4])
        self.assertEqual(data.count, 6)
        self.assertEqual(data.capacity, 16)

    def insert_big_buffer(self):
        data = create_array_to_test(16)
        data.insert(1, 20)
        self.assertListEqual([element for element in data], [0, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(data.count, 17)
        self.assertEqual(data.capacity, 32)

    def delete_invalid_position(self):
        data = create_array_to_test(5)
        self.assertRaises(IndexError, data.delete(-1))
        self.assertRaises(IndexError, data.delete(9))
        
    def delete_same_buffer(self):
        data = create_array_to_test(5)
        data.delete(3)
        self.assertListEqual([element for element in data], [0, 1, 2, 4])
        self.assertEqual(data.count, 4)
        self.assertEqual(data.capacity, 16)

    def delete_smaller_buffer(self):
        data = create_array_to_test(17)
        data.delete(0)
        self.assertListEqual([element for element in data], [i for i in range(1, 17)])
        self.assertEqual(data.count, 16)
        self.assertEqual(data.capacity, 21)


if __name__ == '__main__':
    unittest.main()



