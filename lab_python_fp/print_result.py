def print_result(func):
    def _wrapper(*args, **kwargs):
        print(func.__name__)
        result = func(*args, **kwargs)
        if isinstance(result,list):
            for i in result:
                print(i)
        elif isinstance(result,dict):
            for i in result.keys():
                print(i ,'=', result[i])
        else:
            print(result)
        return result
    return _wrapper

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]

def main():
    test_1()
    test_2()
    test_3()
    test_4()
if __name__ == '__main__':
    main()
