import unittest
from lab_python_fp.field import field
from lab_python_fp.sort import sort_1,sort_2

class Test_field(unittest.TestCase):
    def setUp(self):
        self.goods=[{'title': 'Окно', 'color': 'white'},
        {'title': 'Шторы', 'price': int(1e9), 'color': '', 'name': '', 'addText': 'из будущего'}]
        self.data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

    def test1(self):
        test1=list(field(self.goods,'title'))
        correct = ['Окно', 'Шторы']
        self.assertEqual(test1, correct)

    def test2(self):
        test2 = list(field(self.goods, 'title', 'price'))
        correct = [{'title':'Окно'}, {'title': 'Шторы', 'price': int(1e9)}]
        self.assertEqual(test2, correct)

    def test_sort(self):
        self.assertEqual(sort_1(self.data),[123, 100, -100, -30, 30, 4, -4, 1, -1, 0])

if __name__=='__main__':
    unittest.main()
