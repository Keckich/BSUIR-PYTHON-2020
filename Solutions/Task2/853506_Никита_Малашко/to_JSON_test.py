import unittest
from to_JSON import to_json
from json import dumps


class TestToJson(unittest.TestCase):
    def test_number(self):
        self.assertEqual(to_json(10), dumps(10))
        self.assertEqual(to_json(10.5), dumps(10.5))

    def test_str(self):
        self.assertEqual(to_json('opa f5'), dumps('opa f5'))

    def test_bool(self):
        self.assertEqual(to_json(True), dumps(True))

    def test_none(self):
        self.assertEqual(to_json(None), dumps(None))

    def test_list(self):
        self.assertEqual(to_json([1, 2, ('d', 3, 45), 'ewr', {4: 22, 'q': 'a'}]),
                         dumps([1, 2, ('d', 3, 45), 'ewr', {4: 22, 'q': 'a'}]))

    def test_dict(self):
        self.assertEqual(to_json({4: 'dsd', '5': 322, (323): 'asdas'}), dumps({4: 'dsd', '5': 322, (323): 'asdas'}))


if __name__ == 'main':
    unittest.main()
