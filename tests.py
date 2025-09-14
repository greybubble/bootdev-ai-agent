import unittest
import os
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        self.get_files_info = get_files_info

    def test_wd(self):
        result = self.get_files_info("calculator", ".")
        expected = f'''Result for current directory:
 - main.py: file_size={os.path.getsize("./calculator/main.py")} bytes, is_dir=False
 - tests.py: file_size={os.path.getsize("./calculator/tests.py")} bytes, is_dir=False
 - pkg: file_size={os.path.getsize("./calculator/pkg")} bytes, is_dir=True'''
        print(result)
        
        self.assertEqual(result, expected)

    def test_pkg(self):
        result = self.get_files_info("calculator", "pkg")
        expected = f'''Result for 'pkg' directory:
 - render.py: file_size={os.path.getsize("./calculator/pkg/render.py")} bytes, is_dir=False
 - calculator.py: file_size={os.path.getsize("./calculator/pkg/calculator.py")} bytes, is_dir=False'''
        print(result)

        self.assertEqual(result, expected)

    def test_bin(self):
        result = self.get_files_info("calculator", "/bin")
        expected = '''Result for '/bin' directory:
    Error: Cannot list "/bin" as it is outside the permitted working directory'''
        print(result)

        self.assertEqual(result, expected)

    def test_pd(self):
        result = self.get_files_info("calculator", "../")
        expected = '''Result for '../' directory:
    Error: Cannot list "../" as it is outside the permitted working directory'''
        print(result)

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()