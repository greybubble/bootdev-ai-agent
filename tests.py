import unittest
import os
from functions.get_file_content import get_file_content

class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        self.get_file_content = get_file_content

    # def test_lorem(self):
    #     result = self.get_file_content("calculator", "lorem.txt")
    #     print(f'File length: {len(result)} bytes')
    #     print(f'File Contents:')
    #     print()
    #     print(result)
        
    def test_main(self):
        result = self. get_file_content("calculator", "main.py")
        print()
        print(f'File length: {len(result)} bytes')
        print(f'File Contents:')
        print()
        print(result)
        print()

    def test_pkg(self):
        result = self. get_file_content("calculator", "pkg/calculator.py")
        print()
        print(f'File length: {len(result)} bytes')
        print(f'File Contents:')
        print()
        print(result)
        print()

    def test_bin(self):
        result = self. get_file_content("calculator", "/bin/cat")
        print()
        print(f'File length: {len(result)} bytes')
        print(f'File Contents:')
        print()
        print(result)
        print()

    def test_does_not_exist(self):
        result = self. get_file_content("calculator", "pkg/does_not_exist.py")
        print()
        print(f'File length: {len(result)} bytes')
        print(f'File Contents:')
        print()
        print(result)
        print()



if __name__ == "__main__":
    unittest.main()