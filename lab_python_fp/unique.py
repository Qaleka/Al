from lab_python_fp.gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case',False)
        self.iter = set(items)
        self.used = set()

    def __next__(self):
        count=0
        for i in self.iter:
            if i not in self.used:
                if isinstance(i, str):
                    if not self.ignore_case:
                        self.used.add(i)
                        return i
                    elif i.lower() not in self.used:
                        self.used.add(i.lower())
                        return i.lower()
                    else:
                        count+=1
                else:
                    self.used.add(i)
                    return i
            if len(set(self.used)) == len(set(self.iter)):
                raise StopIteration
            if self.ignore_case==True and len(set(self.used))==(len(set(self.iter))-count):
                raise StopIteration

    def __iter__(self):
        return self

def main():
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for i in Unique(data):
        print(i, end=" ")
    print()

    data = gen_random(10, 1, 3)
    for i in Unique(data):
        print(i, end=" ")
    print()

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for i in Unique(data):
        print(i, end=" ")
    print()

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'b']
    for i in Unique(data, ignore_case=True):
        print(i, end=" ")
    print()



if __name__ == '__main__':
    main()
