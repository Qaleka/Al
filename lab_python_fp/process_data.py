import json
import sys
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.field import field

@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True))

@print_result
def f2(arg):
    return list(filter(lambda x: x[:11].lower() == 'программист', arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))

@print_result
def f4(arg):
    return [job+', зарплата '+str(salary)+' руб.' for job,salary in zip(arg,list(gen_random(len(arg),100000,200000)))]

def main():
    path = r'C:\Users\Андрей\Desktop\lab3\data_light.json'
    with open(path, encoding='UTF-8') as f:
        data = json.load(f)

    with cm_timer_1():
        f4(f3(f2(f1(data))))


if __name__ == '__main__':
    main()
