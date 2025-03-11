from Cython.Build import cythonize
from setuptools import setup, Extension

ext = Extension(
    name="fairino",
    sources=["linux/fairino/Robot.py"]
)

setup(
    name="fairino",
    ext_modules=cythonize(ext)
)
