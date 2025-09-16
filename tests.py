import unittest
import os
from functions.write_file_content import write_file

class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        self.write_file = write_file

    def test_lorem(self):
        result = self.write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)

    def test_morelorem(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)

    def test_temp(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)

    def test_new_dir(self):
        result = write_file("calculator", "temp/new_file.txt", "Checking that a new directory is created.")

if __name__ == "__main__":
    unittest.main()