import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2,result)
    def test_subtract(self):
        result = rpn.calculate("4 6 -")
        self.assertEqual(-2,result)
    def test_multiply(self):
        result = rpn.calculate("5 7 *")
        self.assertEqual(35,result)
    def test_negative_multiply(self):
        result = rpn.calculate("-3 5 *")
        self.assertEqual(-15,result)
    def test_divide(self):
        result = rpn.calculate("7 5 /")
        self.assertEqual(1.4,result)
    def test_toomany(self):
        with self.assertRaises(TypeError):
            #This enables you to give expected error outputs
            result = rpn.calculate('1 2 3 +')
    def test_add_subtract(self):
        result = rpn.calculate("1 2 + 5 -")
        self.assertEqual(-2, result)
    def test_multiply_subtract(self):
        result = rpn.calculate("4 5 * 6 -")
        self.assertEqual(14, result)


if __name__ == '__main__':
    unittest.main()
