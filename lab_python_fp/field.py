def field(items, *args):
    size = len(args)
    assert size > 0
    buff = {}
    for item in items:
        flag=True
        count = 0
        for arg in args:
           count +=1
           if item.get(arg) is not None:
               buff[arg] = item[arg]
               flag = False
               if size == 1:
                    yield buff[arg]
               elif count==size:
                    yield buff
                    buff.clear()
           elif count==size and flag==False:
               yield buff
               buff.clear()

def main():
    goods = [
        {'title': None, 'price': None, 'color': None},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'name': 'Skip me', 'addText': 'please'},
        {'title': 'Окно', 'color': 'white'},
        {'title': 'Шторы', 'price': int(1e9), 'color': '', 'name': '', 'addText': 'из будущего'}
    ]
    test = field(goods,'title')
    print("-----One field------")
    for i in test:
        print(i)
    print("-----Two fields------")
    test = field(goods, 'title','price')
    for i in test:
        print(i)
    print("-----Many fields------")
    test = field(goods, 'title', 'price', 'color', 'addText', 'name')
    for i in test:
        print(i)

if __name__ == '__main__':
    main()
