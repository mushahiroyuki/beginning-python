#ファイル名 Chapter16/listing16-2.py （test_my_math2.py）
import unittest, my_math2

class ProductTestCase(unittest.TestCase):

    def test_integers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = my_math2.product(x, y)
                self.assertEqual(p, x * y, 'Integerの乗算に失敗しました')

    def test_floats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x / 10
                y = y / 10
                p = my_math2.product(x, y)
                self.assertEqual(p, x * y, 'Floatの乗算に失敗しました')

if __name__ == '__main__': unittest.main()
