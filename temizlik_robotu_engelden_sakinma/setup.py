#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
   packages=['temizlik_robotu_engelden_sakinma'],
   package_dir={'': 'src'}
)

setup(**d)
