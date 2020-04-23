import unittest
from decorator import cached, example1


class TestDecorator(unittest.TestCase):

    @cached
    def example(self, x, y):
        return x ** y

    def test_example(self):
        self.assertEqual(self.example(5, 2), 25)
        self.assertEqual(self.example(5, 2), 'Result is 25')
        self.assertEqual(example1(3, 4, 1), 82)
        self.assertEqual(example1(3, 4, 1), 'Result is 82')


if __name__ == 'main':
    unittest.main()
