from __future__ import unicode_literals
import time
from operator import attrgetter

S1 = b'a'
S2 = b'b'
S3 = b'c'
S4 = b'd'
S5 = b'e'
S6 = b'f'


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


methoddispatch = {
    S1: attrgetter('s1'),
    S2: attrgetter('s2'),
    S3: attrgetter('s3'),
    S4: attrgetter('s4'),
    S5: attrgetter('s5'),
    S6: attrgetter('s6')}


class DictAttrGetter(object):
    def dictattrgettrdispatch(self, arg):
        methoddispatch[arg](self)(arg)

    def s1(self, arg):
        pass

    def s2(self, arg):
        pass

    def s3(self, arg):
        pass

    def s4(self, arg):
        pass

    def s5(self, arg):
        pass

    def s6(self, arg):
        pass


def speed_test(f):
    start = time.time()
    for x in xrange(100000):
        for x in (S1, S1, S1, S1, S2, S2, S2, S3, S3, S4, S5, S6):
            f(x)

    print f.__name__, time.time() - start


if __name__ == '__main__':
    speed_test(ifelif)
    speed_test(dictdefinedispatch)
    speed_test(dictdispatch)
    DAG = DictAttrGetter()
    speed_test(DAG.dictattrgettrdispatch)
