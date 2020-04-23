import unittest
from external_sort import external_sort, file_size


class TestSort(unittest.TestCase):
    def setUp(self):
        self.filename = 'numbers_test'

    def test_sort(self):
        external_sort(self.filename)
        count = 0
        with open(self.filename) as file:
            size = file_size(file)
            for i in range(size):
                file.seek(0)
                number = int(file.readlines()[i])
                if count > 0:
                    self.assertTrue(number >= number_prev)
                number_prev = number
                count += 1
            self.assertEqual(size, count)


if __name__ == 'main':
    unittest.main()
