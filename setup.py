from setuptools import setup, Command, Extension
from setuptools.command.install import install
from distutils.command.build import build
from distutils.command.build_ext import build_ext
import subprocess

version = '0.4.0';
svnrevision = '4905';

class CustomBuild(build):
    def run(self):
        self.run_command('build_ext')
        build.run(self)

class CustomInstall(install):
    def run(self):
        self.run_command('build_ext')
        self.do_egg_install()

class pycodcif_build_ext(build_ext):
    def run(self):
        subprocess.check_call(['make', 'SVN_VERSION={}'.format(svnrevision)],
                              cwd='cod-tools/src/externals/cexceptions')
        subprocess.check_call(['make', '--assume-old', 'cif_grammar.y', 'SVN_VERSION={}'.format(svnrevision)],
                              cwd='cod-tools/src/components/codcif')
        build_ext.run(self)

class pycodcif_test(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        from pycodcif import parse
        from tempfile import NamedTemporaryFile
        with NamedTemporaryFile() as f:
            f.write('data_test _tag value')
            f.flush()
            cif = parse( f.name )

setup(
    name="pycodcif",
    version=version,
    author="COD development team",
    description="COD CIF v1.1 parser",
    long_description="COD CIF v1.1 parser",
    author_email="grazulis@ibt.lt",
    maintainer="Andrius Merkys",
    maintainer_email="andrius.merkys@gmail.com",
    packages=['pycodcif'],
    package_dir={'pycodcif': 'cod-tools/src/components/pycodcif'},
    url="http://wiki.crystallography.net/cod-tools",
    license="GPLv2",
    cmdclass={'build_ext': pycodcif_build_ext,
              'build': CustomBuild,
              'install': CustomInstall,
              'test': pycodcif_test},
    ext_modules=[
        Extension('pycodcif._pycodcif',
                  ['cod-tools/src/components/pycodcif/pycodcif.c',
                   'cod-tools/src/components/pycodcif/pycodcif.i'],
                  libraries=['codcif', 'cexceptions'],
                  library_dirs=['cod-tools/src/components/codcif/lib',
                                'cod-tools/src/externals/cexceptions/lib'],
                  include_dirs=['cod-tools/src/externals/cexceptions',
                                'cod-tools/src/externals/getoptions',
                                'cod-tools/src/components/codcif']),
                ],
)
