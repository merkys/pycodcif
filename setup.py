from setuptools import setup, find_packages

version = '1.0.0';

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
    license="GPLv2"
)
