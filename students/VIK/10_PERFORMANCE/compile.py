from distutils.core import setup
from Cython.Build import cythonize

setup(name='Test One', ext_modules=cythonize("calc1.pyx"),)

# run in cmd via: python compile.py build_ext --inplace