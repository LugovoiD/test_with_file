import unittest
from os.path import abspath
from methods.print_string import print_string_from_file, return_files_lines
from ddt import ddt, data
import io
import sys


@ddt
class TestPrintingLine(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_for_test = abspath('files/calling_list.txt')

    def test_ok(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_string_from_file(self.file_for_test, 2)
        printed = captured_output.getvalue().replace("\n", "")
        expected = return_files_lines(self.file_for_test, 2)
        err_msg = f'Printed string is not equal to expected. Printed: {printed} . Expected: {expected}'
        self.assertMultiLineEqual(printed, expected, err_msg)

    def test_raise_type_error_for_file_path(self):
        with self.assertRaises(TypeError):
            print_string_from_file(2, 2)

    def test_raise_type_error_for_number(self):
        with self.assertRaises(TypeError):
            print_string_from_file(self.file_for_test, "")

    @data(-2, 0)
    def test_raise_error_with_negative_or_zero(self, param):
        with self.assertRaises(ArithmeticError):
            print_string_from_file(self.file_for_test, param)

    def test_empty_file(self):
        empty_file = abspath('files/empty.txt')
        with self.assertRaises(Exception):
            print_string_from_file(empty_file, 1)

    def test_raise_error_number_greater_that_file_len(self):
        with self.assertRaises(Exception):
            print_string_from_file(self.file_for_test, 100)


if __name__ == '__main__':
    unittest.main()
