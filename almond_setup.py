from Cython.Build import cythonize
from setuptools import setup

setup(name="Robot", ext_modules=cythonize("linux/fairino/Robot.py"))
