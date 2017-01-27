from setuptools import setup, find_packages, Extension
from distutils.command.build_ext import build_ext
import subprocess

version = '1.0.0';

class pycodcif_build_ext(build_ext):
    def run(self):
        subprocess.check_call(['make'],
                              cwd='cod-tools/src/externals/cexceptions')
        subprocess.check_call(['make'],
                              cwd='cod-tools/src/components/codcif')
        build_ext.run(self)

setup(
    name="pycodcif",
    version=version,
    author="COD development team",
    description="COD CIF parser",
    long_description="COD CIF parser",
    author_email="grazulis@ibt.lt",
    maintainer="Andrius Merkys",
    maintainer_email="andrius.merkys@gmail.com",
    packages=find_packages(),
    url="http://wiki.crystallography.net/cod-tools",
    license="GPLv2",
    cmdclass={'build_ext': pycodcif_build_ext},
    ext_modules=[
        # Extension('cexceptions',
                  # ['cod-tools/src/externals/cexceptions/allocx.c',
                   # 'cod-tools/src/externals/cexceptions/cexceptions.c',
                   # 'cod-tools/src/externals/cexceptions/cxprintf.c',
                   # 'cod-tools/src/externals/cexceptions/stdiox.c',
                   # 'cod-tools/src/externals/cexceptions/stringx.c'],
                   # include_dirs=['cod-tools/src/externals/cexceptions']),
                   # 
        # Extension('codcif', [
                  # 'cod-tools/src/externals/cexceptions/allocx.c',
                  # 'cod-tools/src/externals/cexceptions/cexceptions.c',
                  # 'cod-tools/src/externals/cexceptions/cxprintf.c',
                  # 'cod-tools/src/externals/cexceptions/stdiox.c',
                  # 'cod-tools/src/externals/cexceptions/stringx.c',
                  # 'cod-tools/src/components/codcif/cif.c',
                  # 'cod-tools/src/components/codcif/cifmessage.c',
                  # 'cod-tools/src/components/codcif/common.c',
                  # 'cod-tools/src/components/codcif/yy.c',
                  # 'cod-tools/src/components/codcif/cif_grammar_flex.c',
                  # 'cod-tools/src/components/codcif/cif_lexer.c',
                  # 'cod-tools/src/components/codcif/cif_options.c',
                  # 'cod-tools/src/components/codcif/datablock.c',
                  # 'cod-tools/src/externals/getoptions/getoptions.c'],
                  # include_dirs=['cod-tools/src/externals/cexceptions',
                                # 'cod-tools/src/externals/getoptions',
                                # 'cod-tools/src/components/codcif'],
                  # extra_compile_args=['-DYYDEBUG=1', '-D_YACC_']),
    
        Extension('_ccifparser',
                  ['cod-tools/src/lib/python2.7/dist-packages/cod/ccifparser/ccifparser.c',
                   'cod-tools/src/lib/python2.7/dist-packages/cod/ccifparser/ccifparser.i'],
                  include_dirs=['cod-tools/src/externals/cexceptions',
                                'cod-tools/src/externals/getoptions',
                                'cod-tools/src/components/codcif']),

        # Extension('codcif', [
                # 'cod-tools/src/externals/cexceptions/allocx.c',
                # 'cod-tools/src/externals/cexceptions/cexceptions.c',
                # 'cod-tools/src/externals/cexceptions/cxprintf.c',
                # 'cod-tools/src/externals/cexceptions/stdiox.c',
                # 'cod-tools/src/externals/cexceptions/stringx.c',
                # 'cod-tools/src/components/codcif/cif.c',
                # 'cod-tools/src/components/codcif/cifmessage.c',
                # 'cod-tools/src/components/codcif/common.c',
                # 'cod-tools/src/components/codcif/yy.c',
                # 'cod-tools/src/components/codcif/cif_grammar_flex.c',
                # 'cod-tools/src/components/codcif/cif_lexer.c',
                # 'cod-tools/src/components/codcif/cif_options.c',
                # 'cod-tools/src/components/codcif/datablock.c',
                # 'cod-tools/src/externals/getoptions/getoptions.c',
              # ],
              # include_dirs=['cod-tools/src/externals/cexceptions',
                            # 'cod-tools/src/externals/getoptions',
                            # 'cod-tools/src/components/codcif'],
              # extra_compile_args=['-DYYDEBUG=1', '-D_YACC_'])

          ],
)
