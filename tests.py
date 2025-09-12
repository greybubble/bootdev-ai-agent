import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        self.get_files_info = get_files_info

    def test_wd(self):
        result = self.get_files_info("calculator", ".")
        expected = '''Result for current directory:
 - main.py: file_size=719 bytes, is_dir=False
 - tests.py: file_size=1331 bytes, is_dir=False
 - pkg: file_size=44 bytes, is_dir=True'''
        
        print(expected)
        self.assertEqual(result, expected)

    def test_pkd(self):
        result = self.get_files_info("calculator", "pkg")
        expected = '''Result for 'pkg' directory:
 - calculator.py: file_size=1721 bytes, is_dir=False
 - render.py: file_size=376 bytes, is_dir=False'''
        print(expected)
        self.assertEqual(result, expected)

    def test_bin(self):
        result = self.get_files_info("calculator", "/bin")
        expected = '''Result for '/bin' directory:
    Error: Cannot list "/bin" as it is outside the permitted working directory'''
        print(expected)
        self.assertEqual(result, expected)

    def test_pd(self):
        result = self.get_files_info("calculator", "../")
        expected = '''Result for '../' directory:
    Error: Cannot list "../" as it is outside the permitted working directory'''
        print(expected)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()