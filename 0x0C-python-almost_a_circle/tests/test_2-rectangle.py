#!/usr/bin/python3
"""Module that test all the attribute of the rectangle"""
import sys
import io
import unittest
sys.path.append("/home/libzpc/Programming_Document/all_alx_task/"
                "alx-higher_level_programming/0x0C-python-almost_a_circle")
from models.rectangle import Rectangle


class Rectangle_TestCase(unittest.TestCase):
    """Class that uses unittest to test rectangle"""
    def test_constructor(self):
        rect = Rectangle(10, 12, 3, 4, 9)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 9)

    def test_setter_and_getter(self):
        rect = Rectangle(10, 12, 3, 4, 9)

        rect.width = 20
        self.assertEqual(rect.width, 20)

        rect.height = 23
        self.assertEqual(rect.height, 23)

        rect.x = 15
        self.assertEqual(rect.x, 15)

        rect.y = 45
        self.assertEqual(rect.y, 45)

    def test_width(self):
        rect = Rectangle(20, 10, 7, 4)
        rect.width = 34
        print(rect.width)
        self.assertEqual(rect.width, 34)

    def test_width_exception(self):
        rect = Rectangle(32, 23)
        with self.assertRaises(ValueError):
            rect.width = -5

    def test_height(self):
        rect = Rectangle(20, 10, 7, 4)
        rect.height = 34
        self.assertEqual(rect.height, 34)

    def test_height_exception(self):
        rect = Rectangle(32, 23)
        with self.assertRaises(ValueError):
            rect.height = -5

    def test_x(self):
        rect = Rectangle(20, 10, 7, 4)
        rect.x = 15
        self.assertEqual(rect.x, 15)

    def test_x_exception(self):
        rect = Rectangle(32, 23)
        with self.assertRaises(ValueError):
            rect.x = -5

    def test_width_typeError(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect = Rectangle("Hey", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect = Rectangle(True, 2)

    def test_height_typeError(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect = Rectangle(1, "Hey")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect = Rectangle(2, True)

    def test_x_typeError(self):
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            rect = Rectangle(2, 5, "Hey")
        with self.assertRaisesRegex(TypeError, "x must be integer"):
            rect = Rectangle(3, 1, True)

    def test_y_typeError(self):
        with self.assertRaisesRegex(TypeError, "y must be integer"):
            rect = Rectangle(2, 5, 6, "Hey")
        with self.assertRaisesRegex(TypeError, "y must be integer"):
            rect = Rectangle(3, 1, 8, True)

    def test_y(self):
        rect = Rectangle(20, 10, 7, 4)
        rect.y = 12
        self.assertEqual(rect.y, 12)

    def test_y_exception(self):
        rect = Rectangle(32, 23)
        with self.assertRaises(ValueError):
            rect.y = -5

    def test_area_ans(self):
        rect = Rectangle(5, 10)
        ans = rect.area()
        self.assertEqual(ans, 50)

    def test_with_parameters_passed(self):
        rect = Rectangle(5, 20, 23, 11, 5)
        ans = rect.area()
        self.assertEqual(ans, 100)

    def setUp(self):
        self.saved_stdout = sys.stdout

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_display_strings_check(self):
        r1 = Rectangle(4, 6)
        expected_output_r1 = "####\n####\n####\n####\n####\n####\n"

        sys.stdout = io.StringIO()
        r1.display()
        output_r1 = sys.stdout.getvalue()
        sys.stdout = self.saved_stdout

        self.assertEqual(output_r1, expected_output_r1)

        r2 = Rectangle(2, 2)
        expected_output_r2 = "##\n##\n"

        sys.stdout = io.StringIO()
        r2.display()
        output_r2 = sys.stdout.getvalue()
        sys.stdout = self.saved_stdout
        self.assertEqual(output_r2, expected_output_r2)

    def test_magic_output(self):
        r1 = Rectangle(4, 6, 2, 1, 12)

        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_magic_output_1(self):
        r = Rectangle(4, 6, 2, 1, 12)
        r.width = 8
        r.height = 10
        r.x = 3
        r.y = 5
        self.assertEqual(str(r), "[Rectangle] (12) 3/5 - 8/10")

    def test_display_in_respect_to_x_and_y_axis(self):
        r1 = Rectangle(2, 3, 2, 2)
        expected_output_r1 = "\n\n  ##\n  ##\n  ##\n"

        sys.stdout = io.StringIO()
        r1.display()
        output_r1 = sys.stdout.getvalue()
        sys.stdout = self.saved_stdout

        self.assertEqual(output_r1, expected_output_r1)

        r2 = Rectangle(2, 2)
        expected_output_r2 = " ###\n ###\n"

        sys.stdout = io.StringIO()
        r2.display()
        output_r2 = sys.stdout.getvalue()
        sys.stdout = self.saved_stdout
        self.assertEqual(output_r2, expected_output_r2)


if __name__ == "__main__":
    unittest.main()
