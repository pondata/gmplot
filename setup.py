import os
from setuptools import setup, find_packages

__version__ = '1.2.0'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'gmplot2',
    version = __version__,
    author = 'Justin Oberg',
    author_email = 'justin@pondata.com',
    url = 'https://github.com/pondata/gmplot',
    description = 'Provide a matplotlib like interface to plotting data with Google Maps',
    long_description=read('README.rst'),
    license='MIT',
    keywords='python wrapper google maps',
    packages = find_packages(),
    include_package_data=True,
    package_data = {
        'gmplot': ['markers/*.png'],
    },
    install_requires=['requests'],
)
