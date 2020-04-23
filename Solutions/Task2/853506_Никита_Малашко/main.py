import unittest
from from_JSON_test import TestFromJson
from to_JSON_test import TestToJson
from decorator_test import TestDecorator
from vector_test import TestVector
from sort_test import TestSort

while True:
    print('Print numbers for test:\n 1. Sort\n 2. to_JSON\n 3. Vector\n 4. Decorator\n 5. from_JSON\n 0. Exit\n')
    inpt = int(input())
    if inpt is 1:
        test = unittest.defaultTestLoader.loadTestsFromTestCase(TestSort)
        unittest.TextTestRunner().run(test)
    elif inpt is 2:
        test = unittest.defaultTestLoader.loadTestsFromTestCase(TestToJson)
        unittest.TextTestRunner().run(test)
    elif inpt is 3:
        test = unittest.defaultTestLoader.loadTestsFromTestCase(TestVector)
        unittest.TextTestRunner().run(test)
    elif inpt is 4:
        test = unittest.defaultTestLoader.loadTestsFromTestCase(TestDecorator)
        unittest.TextTestRunner().run(test)
    elif inpt is 5:
        test = unittest.defaultTestLoader.loadTestsFromTestCase(TestFromJson)
        unittest.TextTestRunner().run(test)
    elif inpt is 0:
        exit(0)
