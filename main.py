from operator import itemgetter


class Student:
    """Студент"""

    def __init__(self, id, Fio, age, rec_book, group_id):
        self.id = id
        self.Fio = Fio
        self.age = age
        self.rec_book = rec_book
        self.group_id = group_id


class Group:
    """Группа"""

    def __init__(self, id, index):
        self.id = id
        self.index = index


class StudentsGroup:
    """
    Студенты в группе
    """

    def __init__(self, group_id, student_id):
        self.student_id = student_id
        self.group_id = group_id


# Группы
groups = [
    Group(1, 'ИУ5-31Б'),
    Group(2, 'ИУ5-32Б'),
    Group(3, 'ИУ5-33Б'),

    # Для связи М-М
    Group(11, 'РК7-11Б'),
    Group(22, 'РК7-22Б'),
    Group(33, 'РК7-33Б'),
]

# Студенты
students = [
    Student(1, 'Петров Ю.Г', 19, '38A180', 1),
    Student(2, 'Иванченко В.О', 21,'38A181', 1),
    Student(3, 'Шаляпин Н.Г', 17,'38A182', 2),
    Student(4, 'Сколов Н.А', 24,'38A183', 2),
    Student(5, 'Клемент А.Н', 18,'38A184', 3),
    Student(6, 'Поляков Д.Ю', 19,'38A185', 3)
]
# Студенты в группах(связь М-М)
students_group = [
    StudentsGroup(1, 1),
    StudentsGroup(1, 2),
    StudentsGroup(2, 3),
    StudentsGroup(2, 4),
    StudentsGroup(3, 5),
    StudentsGroup(3, 6),

    StudentsGroup(11, 1),
    StudentsGroup(11, 2),
    StudentsGroup(22, 3),
    StudentsGroup(22, 4),
    StudentsGroup(33, 5),
    StudentsGroup(33, 6),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим 
    one_to_many = [
        (s.Fio, s.age, s.rec_book, g.index)
        for s in students
        for g in groups
        if s.group_id == g.id]

    # Соединение данных многие-ко-многим
    many_to_many = [
        (s.Fio, s.age, s.rec_book, [g.index for g in groups if g.id == s_g.group_id][0])
        for s in students
        for s_g in students_group
        if s.id == s_g.student_id
    ]

#Задание 1: найти всех стужентов фамилия, которых начинается на букву 'П' и вывести их группу
    print('Задание №1')
    res_1 = list(filter(lambda x: x[0][0] == 'П', one_to_many))
    print(res_1)
    for s_fio, s_a, s_b, g_i in res_1:
        print(f'Студент {s_fio} в возрасте {s_a} лет, с номером зачетной книжки - {s_b},в группе {g_i}')

#Задание 2: отсортированные список групп по минимальному возрасту студента в группе
    print('Задание №2')
    res_2 = []
    s_age = []
    s_fio = {}
    for g in groups:
        st_g = list(filter(lambda x: x[3] == g.index, one_to_many))
        if len(st_g)>0:
            for i in st_g:
                s_age.append(i[1])
                s_fio[i[1]] = i[0]
            s_age_min = min(s_age)
            s_age.clear()
            res_2.append((g.index,s_age_min, s_fio[s_age_min] ))
    res_2 = sorted(res_2, key = itemgetter(1), reverse=False)
    print(res_2)
    for g_i, s_a, s_f in res_2:
        print(f'В группе {g_i} минимальный возраст - {s_a} лет, у студента {s_f}')
#Задание 3: список связанных студентов, отсортированный по номеру зачетной книжки
    print('Задание №3')
    res_3 = sorted(many_to_many, key = itemgetter(2))
    print(res_3)
    for s_f, s_a ,s_r, g_i  in res_3:
        print (f'Зачетная книжка {s_r} студента {s_f} возрастом {s_a} лет, в группе - {g_i} ')
if __name__ == '__main__':
    main()
