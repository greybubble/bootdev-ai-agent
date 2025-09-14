import unittest
import os
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        self.get_files_info = get_files_info

    def test_wd(self):
        result = self.get_files_info("calculator", ".")
        print(f"Result for current directory:")
        print(result)
        

    def test_pkg(self):
        result = self.get_files_info("calculator", "pkg")
        print(f"Result for 'pkg' directory:")
        print(result)


    def test_bin(self):
        result = self.get_files_info("calculator", "/bin")
        print("Result for '/bin' directory:")
        print(result)


    def test_pd(self):
        result = self.get_files_info("calculator", "../")
        print("Result for '../' directory:")
        print(result)



if __name__ == "__main__":
    unittest.main()