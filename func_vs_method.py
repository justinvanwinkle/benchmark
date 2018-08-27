from __future__ import print_function
import time


def speed_test(f):
    lst = range(1000000)
    start = time.time()
    for x in lst:
        f(x)

    print(f.__name__, time.time() - start)


def f(arg):
    pass


class F(object):
    def f(self, arg):
        pass

fo = F()


def f1(arg):
    f(arg)


def f2(arg):
    fo.f(arg)

if __name__ == '__main__':
    speed_test(f1)
    speed_test(f2)
