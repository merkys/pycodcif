from setuptools import setup, Extension
from setuptools.command.install import install
from distutils.command.build import build
from distutils.command.build_ext import build_ext
import subprocess

version = '1.0.0';

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
        subprocess.check_call(['make'],
                              cwd='cod-tools/src/externals/cexceptions')
        subprocess.check_call(['make'],
                              cwd='cod-tools/src/components/codcif')
        build_ext.run(self)

setup(
    name="ccifparser",
    version=version,
    author="COD development team",
    description="COD CIF parser",
    long_description="COD CIF parser",
    author_email="grazulis@ibt.lt",
    maintainer="Andrius Merkys",
    maintainer_email="andrius.merkys@gmail.com",
    packages=['ccifparser'],
    package_dir={'ccifparser': 'cod-tools/src/lib/python2.7/dist-packages/cod/ccifparser'},
    url="http://wiki.crystallography.net/cod-tools",
    license="GPLv2",
    cmdclass={'build_ext': pycodcif_build_ext,
              'build': CustomBuild,
              'install': CustomInstall},
    ext_modules=[
        Extension('ccifparser._ccifparser',
                  ['cod-tools/src/lib/python2.7/dist-packages/cod/ccifparser/ccifparser.c',
                   'cod-tools/src/lib/python2.7/dist-packages/cod/ccifparser/ccifparser.i'],
                  libraries=['codcif', 'cexceptions'],
                  library_dirs=['cod-tools/src/components/codcif/lib',
                                'cod-tools/src/externals/cexceptions/lib'],
                  include_dirs=['cod-tools/src/externals/cexceptions',
                                'cod-tools/src/externals/getoptions',
                                'cod-tools/src/components/codcif']),
                ],
)
