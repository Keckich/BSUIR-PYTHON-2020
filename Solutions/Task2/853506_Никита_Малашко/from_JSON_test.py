import unittest
from from_JSON import from_json, from_json_dict, from_json_number, from_json_list, from_json_str
from json import loads, dumps


class TestFromJson(unittest.TestCase):
    def test_number(self):
        self.assertEqual(from_json(dumps(10)), loads(dumps(10)))
        self.assertEqual(from_json(dumps(10.5)), loads(dumps(10.5)))

    def test_str(self):
        self.assertEqual(from_json(dumps('opa f5')), loads(dumps('opa f5')))

    def test_bool(self):
        self.assertEqual(from_json(dumps(True)), loads(dumps(True)))
        self.assertEqual(from_json(dumps(False)), loads(dumps(False)))

    def test_none(self):
        self.assertEqual(from_json(dumps(None)), loads(dumps(None)))

    def test_list(self):
        temp = [1, 2, ('d', 3, 45, 65.6, None), None, True, False, 'ewr', {4: 22, 'q': 'a', 5.6: 7.3}]
        self.assertEqual(from_json(dumps(temp)), loads(dumps(temp)))

    def test_dict(self):
        temp = {4: 'dsd', '5': 322, 323: [4, '4'], 4.5: True, '3': False, 1: None, 90: {8: '3'}}
        self.assertEqual(from_json(dumps(temp)), loads(dumps(temp)))


if __name__ == 'main':
    unittest.main()
