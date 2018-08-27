from __future__ import unicode_literals
from __future__ import print_function

import time
from operator import attrgetter

S1 = 'a'
S2 = 'b'
S3 = 'c'
S4 = 'd'
S5 = 'e'
S6 = 'f'


def s1(arg):
    pass


def s2(arg):
    pass


def s3(arg):
    pass


def s4(arg):
    pass


def s5(arg):
    pass


def s6(arg):
    pass


def ifelif(arg):
    if arg == S1:
        s1(arg)
    elif arg == S2:
        s2(arg)
    elif arg == S3:
        s3(arg)
    elif arg == S4:
        s4(arg)
    elif arg == S5:
        s5(arg)
    elif arg == S6:
        s6(arg)


dispatch = {
    S1: s1,
    S2: s2,
    S3: s3,
    S4: s4,
    S5: s5,
    S6: s6}


def dictdispatch(arg):
    dispatch[arg](arg)


def dictdefinedispatch(arg):
    defdispatch = {
        S1: s1,
        S2: s2,
        S3: s3,
        S4: s4,
        S5: s5,
        S6: s6}
    defdispatch[arg](arg)


class DictAttrGetter(object):
    def attrgettrdispatch(self, arg):
        method = 'case_' + arg
        getattr(self, method)(arg)

    def case_a(self, arg):
        pass

    def case_b(self, arg):
        pass

    def case_c(self, arg):
        pass

    def case_d(self, arg):
        pass

    def case_e(self, arg):
        pass

    def case_f(self, arg):
        pass


def speed_test(f):
    lst = range(100000)
    start = time.time()
    for x in lst:
        for x in (S1, S1, S1, S1, S2, S2, S2, S3, S3, S4, S5, S6):
            f(x)

    print(f.__name__, time.time() - start)


if __name__ == '__main__':
    speed_test(ifelif)
    speed_test(dictdefinedispatch)
    speed_test(dictdispatch)
    DAG = DictAttrGetter()
    speed_test(DAG.attrgettrdispatch)
