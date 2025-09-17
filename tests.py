import unittest
import os
from functions.run_python_file import run_python_file

class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        self.run_python_file = run_python_file

    def test_no_args(self):
        result = run_python_file("calculator", "main.py")
        print(result)

    def test_addition(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])

    def test_tests(self):
        result = run_python_file("calculator", "tests.py")
        print(result)

    def test_running_outside_wd(self):
        result = run_python_file("calculator", "../main.py")
        print(result)

    def test_nonexistent_file(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)



if __name__ == "__main__":
    unittest.main()