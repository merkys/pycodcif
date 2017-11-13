from pycodcif import CifFile, CifDatablock

def test_build_cif():
    datablock = CifDatablock("new")

    datablock.add_loop( [ '_a', '_b' ], [[1, 2], [3, 4]] )
    datablock.add_loop( [ '_c', '_d', '_e' ], [[1, 2, 3], [3, 4, 4], ['c', 'd', 'e']] )

    cif = CifFile()
    cif.append( datablock )

    datablock['_overwritten'] = 'first'
    assert datablock['_overwritten'] == [ 'first' ]

    datablock['_overwritten'] = 'second'
    assert datablock['_overwritten'] == [ 'second' ]
