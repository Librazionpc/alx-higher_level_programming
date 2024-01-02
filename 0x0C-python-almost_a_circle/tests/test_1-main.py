#!/usr/bin/python3
"""Testing Module"""
import sys
sysport unittest
sys.path.append("/home/libzpc/Programming_Document/all_alx_task/"
                "alx-higher_level_programming/0x0C-python-almost"
                "_a_circle/models")
from base import Base

class Test_Bass_Class(unittest.TestCase):
    """Class that test all base class"""
    def test_float(self):
        base = Base(5.5)
        self.assertEqual(base.id, 5.5)

    def test_long_signed_int(self):
        base = Base(100)
        self.assertEqual(base.id, 100)

    def test_long_unsigned_int(self):
        base = Base(-100)
        self.assertEqual(base.id, -100)

    def test_nb_instance_constant(self):
        base = Base(10)
        for i in range(0, 100):
            base = Base()
        self.assertEqual(base.id, 100)


if __name__ == "__main__":
    unittest.main()
