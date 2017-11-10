from setuptools import setup, Command, Extension

version = '0.8.8'
svnrevision = '5724'

setup(
    name="pycodcif",
    version=version,
    author="COD development team",
    description="COD CIF parser",
    long_description="COD parser for CIF1.1 and CIF2.0 formats",
    author_email="grazulis@ibt.lt",
    maintainer="Andrius Merkys",
    maintainer_email="andrius.merkys@gmail.com",
    packages=['pycodcif'],
    package_dir={'pycodcif': 'cod-tools/src/components/pycodcif'},
    url="http://wiki.crystallography.net/cod-tools/CIF-parser",
    license="GPLv2",
    ext_modules=[
        Extension('pycodcif._pycodcif',
                  ['cod-tools/src/externals/cexceptions/cxprintf.c',
                   'cod-tools/src/externals/cexceptions/stringx.c',
                   'cod-tools/src/externals/cexceptions/allocx.c',
                   'cod-tools/src/externals/cexceptions/stdiox.c',
                   'cod-tools/src/externals/cexceptions/cexceptions.c',

                   'cod-tools/src/components/codcif/cif_options.c',
                   'cod-tools/src/components/codcif/common.c',
                   'cod-tools/src/components/codcif/ciftable.c',
                   'cod-tools/src/components/codcif/cif2_lexer.c',
                   'cod-tools/src/components/codcif/cifvalue.c',
                   'cod-tools/src/components/codcif/cifmessage.c',
                   'cod-tools/src/components/codcif/cif_grammar_flex.c',
                   'cod-tools/src/components/codcif/cif_lexer.c',
                   'cod-tools/src/components/codcif/cif.c',
                   'cod-tools/src/components/codcif/datablock.c',
                   'cod-tools/src/components/codcif/cif_compiler.c',
                   'cod-tools/src/components/codcif/ciflist.c',
                   'cod-tools/src/components/codcif/cif_grammar.tab.c',
                   'cod-tools/src/components/codcif/cif2_grammar.tab.c',

                   'cod-tools/src/components/pycodcif/pycodcif.c',
                   'cod-tools/src/components/pycodcif/pycodcif_wrap.c'],
                  define_macros=[
                    ('_YACC_',None),
                    ('YYDEBUG','1'),
                    ('SVN_VERSION',svnrevision),
                  ],
                  include_dirs=['cod-tools/src/externals/cexceptions',
                                'cod-tools/src/components/codcif']),
                ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
