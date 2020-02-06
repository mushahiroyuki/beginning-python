#ファイル名 Chapter16/listing16-3.py
import unittest, my_math2
from subprocess import Popen, PIPE

class ProductTestCase(unittest.TestCase):

    # ここに以前のテストを挿入

    def test_with_PyChecker(self):
        cmd = 'pychecker', '-Q', my_math2.__file__.rstrip('c')
        pychecker = Popen(cmd, stdout=PIPE, stderr=PIPE)
        self.assertEqual(pychecker.stdout.read(), '')

    def test_with_PyLint(self):
        cmd = 'pylint', '-rn', 'my_math2'
        pylint = Popen(cmd, stdout=PIPE, stderr=PIPE)
        self.assertEqual(pylint.stdout.read(), '')

if __name__ == '__main__': unittest.main()
