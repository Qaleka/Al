import unittest
import rk1

class testRk(unittest.TestCase):
    def setUp(self):
        self.test1 = [('Петров Ю.Г', 19, '38A180', 'ИУ5-31Б'),
                      ('Поляков Д.Ю', 19, '38A185', 'ИУ5-33Б')]
        self.test2 = [('ИУ5-32Б', 17, 'Шаляпин Н.Г'),
                      ('ИУ5-33Б', 18, 'Клемент А.Н'),
                      ('ИУ5-31Б', 19, 'Петров Ю.Г')]
        self.test3 = [('Петров Ю.Г', 19, '38A180', 'ИУ5-31Б'),
                      ('Петров Ю.Г', 19, '38A180', 'РК7-11Б'),
                      ('Иванченко В.О', 21, '38A181', 'ИУ5-31Б'),
                      ('Иванченко В.О', 21, '38A181', 'РК7-11Б'),
                      ('Шаляпин Н.Г', 17, '38A182', 'ИУ5-32Б'),
                      ('Шаляпин Н.Г', 17, '38A182', 'РК7-22Б'),
                      ('Сколов Н.А', 24, '38A183', 'ИУ5-32Б'),
                      ('Сколов Н.А', 24, '38A183', 'РК7-22Б'),
                      ('Клемент А.Н', 18, '38A184', 'ИУ5-33Б'),
                      ('Клемент А.Н', 18, '38A184', 'РК7-33Б'),
                      ('Поляков Д.Ю', 19, '38A185', 'ИУ5-33Б'),
                      ('Поляков Д.Ю', 19, '38A185', 'РК7-33Б')]
    def test1_rk(self):
        self.assertEqual(rk1.task1(rk1.students,rk1.groups),self.test1)
    def test2_rk(self):
        self.assertEqual(rk1.task2(rk1.students,rk1.groups),self.test2)
    def test3_rk(self):
        self.assertEqual(rk1.task3(rk1.students,rk1.students_group),self.test3)

if __name__=='__main__':
    unittest.main()
