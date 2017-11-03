from os import path, listdir
from pycodcif import parse, CifParserException
import sys

def test_upstream():
    for f in listdir('tests/cases'):
        if f.endswith('.inp'):
            base = path.splitext(f)[0]
            yield check_parse, 'tests/cases/{}'.format(f), 'tests/cases/{}.opt'.format(base), 'tests/outputs/{}.out'.format(base)

def check_parse(inp_file, opt_file, out_file):
    sys.argv[0] = 'tests/scripts/cif_parser_test'
    with open(out_file, 'r') as f:
        output_old = f.read()
    options = None
    try:
        with open(opt_file, 'r') as f:
            for opt in f.read().splitlines():
                options = {}
                options[opt] = 1;
    except IOError:
        pass
    finally:
        options = None
    with capture() as output_new:
        try:
            if options is not None:
                parse(inp_file, options)
            else:
                parse(inp_file)
        except CifParserException:
            pass
    assert output_old == output_new[0]

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
