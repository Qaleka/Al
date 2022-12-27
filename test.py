from main import fib
import unittest
import types
class Test_fib(unittest.TestCase):
    def test_not(self):
        self.n = -1
        self.assertEqual(list(fib(self.n)),[])
    def test1(self):
        self.n = 5
        correct = [0, 1, 1, 2, 3]
        self.assertEqual(list(fib(self.n)),correct)
    def test2(self):
        self.n = 10
        correct = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(list(fib(self.n)),correct)
    def test3(self):
        self.n = 29
        correct = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
                   987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811]
        self.assertEqual(list(fib(self.n)),correct)
    def test_lazy(self):
        self.n = 5
        correct = [0, 1, 1, 2, 3]
        self.assertEqual(type(fib(self.n)),types.GeneratorType)

if __name__=='__main__':
    unittest.main()
