from Cython.Build import cythonize
from setuptools import setup

setup(name="fairino", ext_modules=cythonize("linux/fairino/Robot.py"))
