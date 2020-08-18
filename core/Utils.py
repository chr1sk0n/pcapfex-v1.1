# -*- coding: utf8 -*-
__author__ = 'Viktor Winkelmann, ported to python 3 by Christoph  Linke'

from threading import Lock

_printLock = Lock()


# synchronized print
def printl(string):
    with _printLock:
        print(string)
