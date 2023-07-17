#!/usr/bin/python3
"""
Import Bass Class Module
Import unittest Module
"""
import unittest
from models.base import Base



class test_base(unittest.TestCase):
    """
    test class for testing the Base Class
    """
    def test_id(self):
        """
        test id of Base Obj
        """
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

        obj2 = Base(5)
        self.assertEqual(obj2.id, 5)

        obj3 = Base()
        self.assertEqual(obj3.id, 2)


if __name__ == '__main__':
    unittest.main()
