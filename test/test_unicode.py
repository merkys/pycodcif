# -*- coding: utf-8 -*-

from pycodcif import parse, CifParserException
import sys

def test_unicode():
    yield check_parse,  "sąžininga žąsis"
    yield check_parse, u"sąžininga žąsis"

def check_parse(inp_file):
    sys.argv[0] = 'test_unicode'
    with capture() as output:
        try:
            parse(inp_file)
        except CifParserException as e:
            pass
    expect = "test_unicode: sąžininga&nbsp;žąsis: ERROR, could not open file -- no such file or directory.\n"
    assert output[0] == expect

import contextlib

@contextlib.contextmanager
def capture():
    import sys
    from cStringIO import StringIO
    oldout,olderr = sys.stdout, sys.stderr
    try:
        out=[StringIO(), StringIO()]
        sys.stdout,sys.stderr = out
        yield out
    finally:
        sys.stdout,sys.stderr = oldout, olderr
        out[0] = out[0].getvalue()
        out[1] = out[1].getvalue()
