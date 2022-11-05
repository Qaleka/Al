from contextlib import contextmanager
from time import sleep,perf_counter

class cm_timer_1:
    def __init__(self):
        self.start = 0
        self.end = 0

    def __enter__(self):
        self.start = perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = perf_counter()
        print('Time = {:.4f}'.format(self.end-self.start))

@contextmanager
def cm_timer_2():
    start = perf_counter()
    yield
    end = perf_counter()
    print('Time = {:.4f}'.format(end-start))

def main():
    with cm_timer_1():
        sleep(5.5)
    with cm_timer_2():
        sleep(5.5)


if __name__ == '__main__':
    main()
